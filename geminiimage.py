from dotenv import load_dotenv
from google import genai
import os
from google.genai import types
import requests


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

image = "IMG_5413.JPG"
uploaded_file = client.files.upload(file=image)

image2 = "IMG_5411.JPG"
with open(image2, 'rb') as f:
    image_bytes2 = f.read()

client = genai.Client()
response = client.models.generate_content(
    model='gemini-3-flash-preview',
    contents=[
      "What is different between these two images?",
        uploaded_file,
        types.Part.from_bytes(
            data=image_bytes2,
            mime_type='image/png'
        )
    ]
  )

print(response.text)