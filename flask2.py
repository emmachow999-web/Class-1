import os
import json
import requests
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

MODEL = "gemini-2.5-flash-lite" 

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

app = Flask(__name__)
@app.route('/weather', methods=['POST'])
def weather_handler():
    try:
        days = request.args.get('days')
        zip_code = request.args.get('zip_code')
        api_key = os.environ.get("WEATHER_API_KEY")

        response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={zip_code}&days={days}")
        response_obj = json.loads(response.content)

        result = {}
        for day_report in response_obj["forecast"]["forecastday"]:
            date = day_report["date"]
            condition = day_report["day"]["condition"]["text"]
            condition_img = day_report["day"]["condition"]["icon"]
            min_temp = f'{day_report["day"]["mintemp_f"]}F'
            max_temp = f'{day_report["day"]["maxtemp_f"]}F'

            result[date] = {
                "condition": condition,
                "condition_img": condition_img,
                "min_temp": min_temp,
                "max_temp": max_temp,
            }

        return json.dumps(result), 200
    except Exception as e:
        return json.dumps({"error": str(e)}), 500


if __name__ == '__main__':
    app.run