from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()
weather_api_key = os.getenv("WEATHER_API_KEY")

zipCode = input()
days = input()
response = requests.get("http://api.weatherapi.com/v1/forecast.json?key=" + weather_api_key + "&q=" + zipCode + "&days=" + days + "&aqi=no&alerts=no")
response_obj = json.loads(response.content)
weather = response_obj["forecast"]["forecastday"][int(days)-1]["day"]["condition"]["text"]

print ("the weather is: ", weather, "on ", response_obj["forecast"]["forecastday"][int(days)-1]["date"])