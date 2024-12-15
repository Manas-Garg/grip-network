import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, LSTM, Dense, Dropout, Conv1D, MaxPooling1D, Flatten, MultiHeadAttention, LayerNormalization, GlobalAveragePooling1D
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

# Load Data
def load_data(file_path):
    data = pd.read_csv(file_path)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data = data.set_index('timestamp')
    return data

# Preprocess Data
def preprocess_data(data, feature_cols, lookback=30):
    scaler = MinMaxScaler()
    data_scaled = scaler.fit_transform(data[feature_cols].values)

    X, y = [], []
    for i in range(len(data_scaled) - lookback):
        X.append(data_scaled[i:i + lookback])
        y.append(data_scaled[i + lookback])

    X = np.array(X)
    y = np.array(y)
    return X, y, scaler

# Build Hybrid Model (LSTM + CNN + Transformer)
def build_advanced_model(input_shape):
    inputs = Input(shape=input_shape)

    # LSTM branch
    lstm = LSTM(128, return_sequences=True)(inputs)
    lstm = Dropout(0.2)(lstm)

    # CNN branch
    cnn = Conv1D(64, kernel_size=3, activation='relu')(inputs)
    cnn = MaxPooling1D(pool_size=2)(cnn)
    cnn = Flatten()(cnn)

    # Transformer branch
    transformer = MultiHeadAttention(num_heads=4, key_dim=64)(inputs, inputs)
    transformer = LayerNormalization()(transformer)
    transformer = GlobalAveragePooling1D()(transformer)

    # Concatenate branches
    combined = tf.keras.layers.Concatenate()([lstm[:, -1, :], cnn, transformer])
    combined = Dense(128, activation='relu')(combined)
    combined = Dropout(0.3)(combined)
    outputs = Dense(input_shape[1])(combined)

    model = Model(inputs, outputs)
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model

if __name__ == "__main__":
    # Load and preprocess data
    data = load_data("processed/processed_climate_data.csv")
    X, y, scaler = preprocess_data(data, feature_cols=['co2', 'temperature', 'methane'], lookback=30)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build and train model
    model = build_advanced_model((X_train.shape[1], X_train.shape[2]))
    model.fit(X_train, y_train, epochs=50, batch_size=64, validation_data=(X_test, y_test))

    # Save model
    model.save("models/advanced_climate_model.h5")
    print("Advanced climate model saved.")
