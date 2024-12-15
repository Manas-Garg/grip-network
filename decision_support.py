import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load Data
data = np.load("processed/decision_data.npy")
X = data[:, :-1]  # Features
y = data[:, -1]   # Labels

# Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate Model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Decision Support Model Accuracy: {accuracy}")

# Example Recommendation
example_state = np.array([0.5, 0.3, 0.2, 0.7]).reshape(1, -1)
recommendation = clf.predict(example_state)
print(f"Recommended Intervention: {recommendation}")
