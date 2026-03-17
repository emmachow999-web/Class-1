
from dotenv import load_dotenv
import json
import requests
import os

load_dotenv()
nasa_api_key = os.getenv("NASA_API_KEY")

startDate = input("start date (YYYY/MM/DD): ")
endDate = input("end date (YYYY/MM/DD): ")
response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?" + "start_date=" + startDate + "&end_date="  + endDate + "&api_key=" + nasa_api_key )
response_obj = json.loads(response.content)
asteroids = response_obj["near_earth_objects"]

largestName = ""
largestDiameter = 0
largestSpeed = 0

for date in asteroids:
    today = asteroids[date]

    for asteroid in today:
        name = asteroid["name"]
        diameter = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"]
        speed = asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]

    if diameter > largestDiameter:
        largestDiameter = diameter
        largestName = name
        largestSpeed = speed


print ("largest asteroid from inputted date:", largestName)
print("diameter (km):", largestDiameter)
print("speed (km/h):", largestSpeed)
