import json
import requests

pokemonid = input()
response = requests.get("https://pokeapi.co/api/v2/pokemon/" + pokemonid)

if response.status_code != 200: 
    print("this pokemon don't exist", response.status_code)
    
else:
    response_obj = json.loads(response.content)
    stats = response_obj["stats"]

    print("name is: ", response_obj["name"])
    print("height is: ", response_obj["height"])
    print("weight is: ", response_obj["weight"])

    hp = 0
    attack = 0
    defense = 0

    for item in response_obj["stats"]:
        stat_name = item["stat"]["name"]
        stat_value = item["base_stat"]

        if stat_name == "hp":
            hp = stat_value
        if stat_name == "attack":
            attack = stat_value
        if stat_name == "defense":
            defense = stat_value
    
    print("hp: ", hp)
    print("attack: ", attack)
    print("defense", defense)