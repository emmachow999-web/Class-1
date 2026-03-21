
from dotenv import load_dotenv
from typing import NamedTuple
import json
import requests
import os

load_dotenv()
nasa_api_key = os.getenv("NASA_API_KEY")

class Asteroid(NamedTuple):
    diameter: float
    speed: float
    name: str

asteroids = {
"2020-1-1": [{
    "name": "my_asteroid",
    "estimated_diameter": {
        "kilometers": {
            "estimated_diameter_max": 1
        }
    },
    "close_approach_data": [
        {
            "relative_velocity": {
                "kilometers_per_hour": 5
            }
        }
    ]
},
{
    "name": "your_asteroid",
    "estimated_diameter": {
        "kilometers": {
            "estimated_diameter_max": 2
        }
    },
    "close_approach_data": [
        {
            "relative_velocity": {
                "kilometers_per_hour": 6
            }
        }
    ]
}

]
}

startDate = input("start date (YYYY-MM-DD): ")
endDate = input("end date (YYYY-MM-DD): ")
response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?" + "start_date=" + startDate + "&end_date="  + endDate + "&api_key=" + nasa_api_key )
response_obj = json.loads(response.content)
asteroids = response_obj["near_earth_objects"]

largest = Asteroid(name="", diameter=0, speed=0)

for date in asteroids:
    for asteroid in asteroids[date]:
        current = Asteroid(
            name     = asteroid["name"],
            diameter = asteroid["estimated_diameter"]["kilometers"]["estimated_diameter_max"],
            speed    = asteroid["close_approach_data"][0]["relative_velocity"]["kilometers_per_hour"]
        )

        if current.diameter > largest.diameter:
            largest = current


print ("largest asteroid from inputted date:", largest.name)
print("diameter (km):", largest.diameter)
print("speed (km/h):", largest.speed)
