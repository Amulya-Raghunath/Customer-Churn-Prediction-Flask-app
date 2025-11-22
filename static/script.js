async function predictChurn() {
    const payload = {
        gender: document.getElementById("gender").value,
        SeniorCitizen: parseInt(document.getElementById("SeniorCitizen").value),
        Partner: document.getElementById("Partner").value,
        Dependents: document.getElementById("Dependents").value,

        tenure: parseInt(document.getElementById("tenure").value) || 0,
        PhoneService: document.getElementById("PhoneService").value,
        MultipleLines: document.getElementById("MultipleLines").value,
        InternetService: document.getElementById("InternetService").value,
        OnlineSecurity: document.getElementById("OnlineSecurity").value,
        OnlineBackup: document.getElementById("OnlineBackup").value,
        DeviceProtection: document.getElementById("DeviceProtection").value,
        TechSupport: document.getElementById("TechSupport").value,
        StreamingTV: document.getElementById("StreamingTV").value,
        StreamingMovies: document.getElementById("StreamingMovies").value,

        Contract: document.getElementById("Contract").value,
        PaperlessBilling: document.getElementById("PaperlessBilling").value,
        PaymentMethod: document.getElementById("PaymentMethod").value,

        MonthlyCharges: parseFloat(document.getElementById("MonthlyCharges").value) || 0,
        TotalCharges: parseFloat(document.getElementById("TotalCharges").value) || 0
    };

    const response = await fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload)
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h3>Prediction: ${data.prediction}</h3>
        <p>Probability: ${(data.probability).toFixed(2)}%</p>
    `;
}
