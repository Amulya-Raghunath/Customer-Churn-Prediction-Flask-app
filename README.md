# **Telecome Customer Churn Prediction using Flask API and Docker**
This project is an end-to-end **Telecom Customer Churn Prediction System** that uses machine learning to determine whether a customer is likely to churn.
It includes a **Flask API**, **a frontend UI**, and is fully **Dockerized** for easy deployment.
## **Technologies Used**
**1. Jupyter Notebook**-Used for Model building and EDA analysis<br>
**2. Spyder**-Developement and Testing<br>
**3. Flask API**-Backend Usage for prediction<br>
**4. Docker**-Containerized deployment<br>

## **Project Overview**
  <li>Builds a churn prediction ML model using <b>XGBoost</b>.</li>
  <li>Saves preprocessing steps using scikit-learn pipelines.</ul><br></li>
  <li>Flask API exposes a /predict endpoint for real-time predictions.</li>
  <li>Frontend UI sends customer details to the API for prediction.</li>
  <li>Docker runs the entire app using <b>Gunicorn</b> for production.</li>
  
## **Instruction**
### **Run Locally**
**1. Install dependencies** <br>
*pip install -r requirements.txt* <br>
**2. Run Flask app** <br>
*python app.py* 
### **Run using Docker**
**1.Build the Docker image**<br>
*docker build -t churn-flask-app .*<br>
**2.Run the Container**<br>
*docker run -p 5000:5000 churn-flask-app*<br>

