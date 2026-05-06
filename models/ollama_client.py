import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_model(model, prompt):
    response = requests.post(OLLAMA_URL, json={
        "model": model,
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]