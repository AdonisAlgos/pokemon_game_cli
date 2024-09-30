import requests
import json
import random

# Get the list of pokemon from the API
def get_pokemon_list(url):
    response = requests.get(url)
    return json.loads(response.text)['results']

# Get the pokemon's data from the API
def get_pokemon_data(url, pokemon):
    url = "{}/{}/".format(url,pokemon)
    response = requests.get(url)
    return json.loads(response.text)


def create_pokemon_data(data):
    # Format height and weight properly
    height = int(data['height'])
    weight = int(data['weight'])

    height_formatted = height / 10
    weight_formatted = weight / 10

    return {
        "name": data["name"],
        "ability": data['abilities'][0]["ability"],
        "height": height_formatted,
        "weight": weight_formatted,
        "hp": data['stats'][0]["base_stat"],
        "attack": data['stats'][1]["base_stat"],
        "defence": data['stats'][2]["base_stat"],
        "speed": data['stats'][5]["base_stat"],
            }


pokemon_list = get_pokemon_list('https://pokeapi.co/api/v2/pokemon/')

for pokemon in pokemon_list:
    print(pokemon['name'])

# Ask the user to choose a pokemon
player_pokemon_choice = input('Enter your pokemon: ').lower()

player_pokemon_data = get_pokemon_data('https://pokeapi.co/api/v2/pokemon/', player_pokemon_choice)
player_pokemon_data_obj = create_pokemon_data(player_pokemon_data)

# Print the pokemon's data
for (key, value) in player_pokemon_data_obj.items():
    print(f"{key.capitalize()}: {value}")

cpu_pokemon_choice = random.choice(pokemon_list)["name"]
print(cpu_pokemon_choice)
cpu_pokemon_data = get_pokemon_data('https://pokeapi.co/api/v2/pokemon/', cpu_pokemon_choice)
cpu_pokemon_data_obj = create_pokemon_data(cpu_pokemon_data)
print(f"CPU's Pokémon: {cpu_pokemon_data['name']}")


game = True
round_number = 1

while game:
    is_attack = False
    is_defense = False
    if round_number % 2 != 0:
    # Odd rounds: Player 1 attacks, Player 2 defends
        player_1_attack = random.randint(1, 101)
        player_2_defense = random.randint(1, 101)
        if player_pokemon_data_obj["attack"] >= player_1_attack:
             is_attack = True
        else:
             is_attack = False
        if cpu_pokemon_data_obj["defense"] >= player_2_defense:
            is_defense = True
        else:
             is_defense = False
    else:
        player_2_attack = random.randint(1, 101)
        player_1_defense = random.randint(1, 101)





