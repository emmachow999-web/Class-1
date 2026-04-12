import os
import re
from google import genai
from google.genai import types
from dotenv import load_dotenv

# dotenv -f /path/to/.env run python3 app.py
load_dotenv() # load from .env by default in the current directory
    
import json
from flask import Flask, request

MODEL = "gemini-2.5-flash-lite" 

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

app = Flask(__name__)


@app.route('/add_post', methods=['POST'])
def add_post():
    try:
        data = json.loads(request.data)
        num1 = data['num1']
        num2 = data['num2']
        return json.dumps({'sum': int(num1)+int(num2)}), 200
    except Exception as e:
        return json.dumps({'error': str(e)}), 500

def data_url_to_google_types():
    _, media_type, encode_base, content = re.split("data:[;]", data_url)
    return types.Part.from_bytes(
        mime_type = media_type,
        data = content,
    )

def make_story(image_url_with_desc):
    try:
        contents = [
            """
            make a story for the images inputted, 100 words or less
            """,
        ]

        for img_with_desc in image_url_obj:
            contents.append(data_url_to_google_types(img_with_desc["data_url"]))
            contents.append(f"The {i}-th image's description: {img_with_desc['description']}")

        response = client.models.generate_content(
            model = MODEL,
            contents = contents,
        )
        return {
            "summary": response.text
        }
    except Exception as e:
        return {
            "error": f"Exception occured: {e}"
        }

@app.route('/generate_story', methods=['POST'])
def generate_story():
    image_url_obj = json.loads(request.data)
    print(image_url_obj)
    value = json.dumps(make_story(image_url_obj))
    print(value)
    return value, 200

if __name__ == '__main__':
    app.run(debug=True)