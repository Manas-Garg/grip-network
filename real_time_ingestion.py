from kafka import KafkaProducer
import json
import time
import requests

KAFKA_BROKER = "localhost:9092"
TOPIC = "climate_data"

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

DATA_SOURCE_URL = "https://api.carbontracker.org/v1/data"

while True:
    response = requests.get(DATA_SOURCE_URL)
    if response.status_code == 200:
        data = response.json()
        producer.send(TOPIC, value=data)
        print("Data sent to Kafka.")
    else:
        print("Failed to fetch data.")
    time.sleep(60)  # Fetch data every minute
