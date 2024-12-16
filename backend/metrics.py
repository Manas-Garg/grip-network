from prometheus_client import Counter, Histogram, start_http_server
import time

# Metrics Definitions
REQUEST_COUNT = Counter('app_requests_total', 'Total HTTP requests')
REQUEST_LATENCY = Histogram('app_request_latency_seconds', 'Latency of HTTP requests in seconds')

# Start Prometheus Server
start_http_server(8000)

def monitor_request(func):
    def wrapper(*args, **kwargs):
        REQUEST_COUNT.inc()
        start_time = time.time()
        response = func(*args, **kwargs)
        REQUEST_LATENCY.observe(time.time() - start_time)
        return response
    return wrapper

# Example Usage in Flask
from flask import Flask

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
@monitor_request
def predict():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
