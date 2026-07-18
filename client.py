import requests
import json

from config import API_KEY, MODEL, API_URL


def ask(messages):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": MODEL,
        "messages": messages,
    }
    response = requests.post(API_URL, headers=headers, data=json.dumps(payload))
    data = response.json()
    if "choices" not in data:
        print("API returned an error response:")
        print(json.dumps(data, indent=2))
        raise RuntimeError("No 'choices' in API response — check the error above.")
    return data["choices"][0]["message"]["content"]
