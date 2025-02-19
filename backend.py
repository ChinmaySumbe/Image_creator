import os
import requests
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")     # you can use os.getenv() for your local repository.

API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"

headers = {"Authorization": f"Bearer {API_KEY}"}

def generate_image(prompt):
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    print(f"API Response Code: {response.status_code}")
    print(f"API Response Text: {response.text}")

    if response.status_code == 200:
        image = Image.open(io.BytesIO(response.content))
        return image
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")
