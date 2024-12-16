from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Cerebras API Configuration
CEREBRAS_API_URL = "https://api.cerebras.ai/v1/generate"
CEREBRAS_HEADERS = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

# Route: Serve Climate Predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prompt = f"Predict climate metrics based on the following input: {data['input']}"
    payload = {
        "model": "llama3.1-70b",
        "prompt": prompt,
        "max_tokens": 150
    }
    response = requests.post(CEREBRAS_API_URL, headers=CEREBRAS_HEADERS, json=payload)
    prediction = response.json()
    return jsonify(prediction)

# Route: Serve Optimal Interventions
@app.route('/intervene', methods=['POST'])
def intervene():
    data = request.json
    prompt = f"Based on the current state: {data['state']}, suggest optimal interventions."
    payload = {
        "model": "llama3.1-70b",
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(CEREBRAS_API_URL, headers=CEREBRAS_HEADERS, json=payload)
    intervention = response.json()
    return jsonify(intervention)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
