from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
import json
import sqlite3

app = Flask(__name__)

# Load Models
climate_model = load_model("models/advanced_climate_model.h5")
intervention_model_path = "models/advanced_intervention_optimizer.zip"

# Utility: Load Database Records
def query_database(query):
    conn = sqlite3.connect("climate_data.db")
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# Route: Serve Climate Predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    input_data = np.array(data['input']).reshape((1, -1, len(data['input'][0])))
    prediction = climate_model.predict(input_data).tolist()
    return jsonify({"prediction": prediction})

# Route: Serve Optimal Interventions
@app.route('/intervene', methods=['POST'])
def intervene():
    state = request.json.get("state")
    # Mock intervention since advanced RL models require state emulation
    action = np.random.choice(["carbon_capture", "renewable_energy", "afforestation", "geoengineering"])
    return jsonify({"optimal_action": action})

# Route: Fetch Historical Data
@app.route('/history', methods=['GET'])
def history():
    query = "SELECT * FROM climate_data ORDER BY timestamp DESC LIMIT 50;"
    data = query_database(query)
    return jsonify({"history": data})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
