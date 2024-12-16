import requests

CEREBRAS_API_URL = "https://api.cerebras.ai/v1/generate"
CEREBRAS_HEADERS = {
    "Authorization": "Bearer csk-w9kx62etv68c9rkdt382f3dc8vnmerrtr8ewxf55vyd4en29",
    "Content-Type": "application/json"
}

# Decision Support Logic
def real_time_recommendation(state):
    prompt = f"Analyze the state: {state} and provide the best climate interventions."
    payload = {
        "model": "llama3.1-70b",
        "prompt": prompt,
        "max_tokens": 100
    }
    response = requests.post(CEREBRAS_API_URL, headers=CEREBRAS_HEADERS, json=payload)
    return response.json()

if __name__ == "__main__":
    example_state = "High CO2 levels, rising temperatures, and significant deforestation."
    recommendation = real_time_recommendation(example_state)
    print("Recommended Intervention:", recommendation["choices"][0]["text"])
