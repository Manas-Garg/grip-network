import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import load_model

def plot_advanced_predictions(data, model, scaler, lookback=30):
    inputs = scaler.transform(data[-lookback:].reshape(-1, len(data.columns)))
    inputs = np.reshape(inputs, (1, inputs.shape[0], inputs.shape[1]))
    predictions = model.predict(inputs)
    predictions = scaler.inverse_transform(predictions)

    plt.figure(figsize=(10, 6))
    plt.plot(data.index[-50:], data.values[-50:, 0], label="Actual CO2")
    plt.plot(data.index[-50:], predictions.flatten(), label="Predicted CO2")
    plt.legend()
    plt.title("Advanced Climate Predictions")
    plt.show()

if __name__ == "__main__":
    data = pd.read_csv("processed/processed_climate_data.csv")
    model = load_model("models/advanced_climate_model.h5")
    scaler = MinMaxScaler()
    scaler.fit(data[['co2', 'temperature', 'methane']].values)
    plot_advanced_predictions(data[['co2', 'temperature', 'methane']], model, scaler)
