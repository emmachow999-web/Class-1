import json
import requests

pokemonid = input()
response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemonid)

if response.status_code != 200: 
    print("this pokemon don't exist", response.status_code)
    
else:
    response_obj = json.loads(response.content)

    print("name is: ", response_obj["name"])
    print("height is: ", response_obj["height"])
    print("weight is: ", response_obj["weight"])

stats = response_obj["stats"]

hp = stats[0]["base_stat"]
attack = stats[1]["base_stat"]
defense = stats[2]["base_stat"]
print("hp: ", hp)
print("attack: ", attack)
print("defense: ", defense)