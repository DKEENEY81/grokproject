import os
import requests
from dotenv import load_dotenv



load_dotenv()

# Access the API key from .env
api_key = os.getenv("XAI_API_KEY")

if not api_key:
    raise ValueError("API key not found. Please set the XAI_API_KEY in your .env file.")


#Construct headers for the request
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Construct the request payload
payload = {
    "messages": [
        {"role": "system", "content": "You are a brilliant investment manager."},
        {"role": "user", "content": "Starting with 35,000 USD what are some immediate income earning steps I can take to grow this amount?"}
    ],
    "model": "grok-4-0709",
    "stream": False,
    "temperature": 0
}

response = requests.post("https://api.x.ai/v1/chat/completions", headers=headers, json=payload)

# Print the result
if response.ok:
    print(response.json())
else:
    print(f"Request failed: {response.status_code} - {response.text}")





