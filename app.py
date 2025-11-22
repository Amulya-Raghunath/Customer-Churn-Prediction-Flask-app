# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 12:29:31 2025
@author: Amulya
"""

from flask import Flask, jsonify, request, render_template
import pickle
import pandas as pd
import os

app = Flask(__name__)

# -----------------------------
# Load Model + Preprocessor
# -----------------------------
MODEL_DIR = os.path.join(os.getcwd(), "model")

with open(os.path.join(MODEL_DIR, "preprocessor.pkl"), "rb") as f:
    preprocessor = pickle.load(f)

with open(os.path.join(MODEL_DIR, "xgb_model.pkl"), "rb") as f:
    model = pickle.load(f)


# -----------------------------
# Home -> serves index.html
# -----------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -----------------------------
# Prediction API (JSON only)
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json
        df = pd.DataFrame([data])

        # Transform data
        X = preprocessor.transform(df)

        # Predict
        pred = int(model.predict(X)[0])
        prob = float(model.predict_proba(X)[0][1])

        # Avoid NaN
        if pd.isna(prob):
            prob = 0.0

        return jsonify({
            "prediction": "Churn" if pred == 1 else "No Churn",
            "probability": round(prob * 100, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


# -----------------------------
# Health Route
# -----------------------------
@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


# -----------------------------
# Run for Docker
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
