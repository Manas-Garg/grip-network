from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Mock user database
users = {
    "admin": generate_password_hash("password123")
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users and check_password_hash(users[username], password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route('/predict', methods=['POST'])
@jwt_required()
def predict():
    return jsonify({"message": "Prediction authorized."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
