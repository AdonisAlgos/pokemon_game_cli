import requests
import json
import random

# Constants for URL and formatting
POKEMON_API_URL = 'https://pokeapi.co/api/v2/pokemon/'
KEY_WIDTH = 8
VALUE_WIDTH = 10

# Get the list of Pokémon from the API
def get_pokemon_list(url):
    response = requests.get(url)
    return response.json()['results']

# Get the Pokémon's data from the API
def get_pokemon_data(url, pokemon):
    response = requests.get(f"{url}{pokemon}/")
    return response.json()

# Create a formatted Pokémon data object
def create_pokemon_data(data):
    height_formatted = data['height'] / 10  # Convert height to meters
    weight_formatted = data['weight'] / 10  # Convert weight to kilograms

    return {
        "name": data["name"],
        "ability": data['abilities'][0]["ability"]["name"],
        "height": height_formatted,
        "weight": weight_formatted,
        "hp": data['stats'][0]["base_stat"],
        "attack": data['stats'][1]["base_stat"],
        "defence": data['stats'][2]["base_stat"],
        "speed": data['stats'][5]["base_stat"],
    }

# Display Pokémon names in a grid
def display_pokemon_list(pokemon_list):
    for index, pokemon in enumerate(pokemon_list):
        print(f"{pokemon['name']:<15}", end='\t\t')
        if (index + 1) % 3 == 0:
            print()  # Move to the next line

# Display Pokémon stats in formatted lines
def display_pokemon_stats(pokemon_data):
    key_value_pairs = list(pokemon_data.items())
    for index, (key, value) in enumerate(key_value_pairs):
        print(f"{key.capitalize():<{KEY_WIDTH}}: {str(value):<{VALUE_WIDTH}}", end='  ')
        if (index + 1) % 3 == 0:
            print()

# Main Game Logic
def play_game(player_pokemon_data, cpu_pokemon_data):
    player_pokemon_name = player_pokemon_data["name"].capitalize()
    cpu_pokemon_name = cpu_pokemon_data["name"].capitalize()

    game = True
    round_number = 1
    print(f"-------------- {player_pokemon_data['name'].upper()} vs {cpu_pokemon_data['name'].upper()} --------------")
    input("Ready to begin the battle? Hit enter to start!")

    while game:
        print(f"\n-------------- Round {round_number} --------------")
        is_player_turn = round_number % 2 != 0

        # Determine attack and defense outcomes
        attack = random.randint(1, 101)
        defense = random.randint(1, 101)

        if is_player_turn:
            is_attack = player_pokemon_data["attack"] >= attack
            is_defense = cpu_pokemon_data["defence"] >= defense

            if is_attack and is_defense:
                cpu_pokemon_data["hp"] -= player_pokemon_data["attack"] / 2
                print(f"Player: {player_pokemon_name} lands a light blow")
                print(f"CPU: {cpu_pokemon_name} takes half damage!")
            elif is_attack:
                cpu_pokemon_data["hp"] -= player_pokemon_data["attack"]
                print(f"Player: {player_pokemon_name} lands a powerful attack!")
                print(f"CPU: {cpu_pokemon_name} takes full damage!")
            else:
                print(f"Player: {player_pokemon_name} tries to attack, but {cpu_pokemon_name} blocks it!")

        else:
            is_attack = cpu_pokemon_data["attack"] >= attack
            is_defense = player_pokemon_data["defence"] >= defense

            if is_attack and is_defense:
                player_pokemon_data["hp"] -= cpu_pokemon_data["attack"] / 2
                print(f"CPU: {cpu_pokemon_name} lands a light blow")
                print(f"Player: {player_pokemon_name} takes half damage!")
            elif is_attack:
                player_pokemon_data["hp"] -= cpu_pokemon_data["attack"]
                print(f"CPU: {cpu_pokemon_name} lands a powerful attack!")
                print(f"Player: {player_pokemon_name} takes full damage!")
            else:
                print(f"CPU: {cpu_pokemon_name} tries to attack, but {player_pokemon_name} blocks it!")

        # Display HP levels after each round
        print(f"\n{player_pokemon_name} HP: {player_pokemon_data['hp']}")
        print(f"{cpu_pokemon_name} HP: {cpu_pokemon_data['hp']}")

        # Check if game ends
        if player_pokemon_data["hp"] <= 0:
            print(f"{player_pokemon_name} has fainted! The CPU's {cpu_pokemon_name} wins!")
            game = False
        elif cpu_pokemon_data["hp"] <= 0:
            print(f"{cpu_pokemon_name} has fainted! The Player's {player_pokemon_name} wins!")
            game = False

        round_number += 1

# Main function to run the game
def main():
    pokemon_list = get_pokemon_list(POKEMON_API_URL)
    display_pokemon_list(pokemon_list)
    print()

    # Ask the user to choose a Pokémon
    player_pokemon_choice = input('\nEnter your pokemon: ').lower()
    print()

    # Get Pokemon data
    player_pokemon_data = create_pokemon_data(get_pokemon_data(POKEMON_API_URL, player_pokemon_choice))
    display_pokemon_stats(player_pokemon_data)
    print()


    # CPU randomly selects a Pokémon
    cpu_pokemon_choice = random.choice(pokemon_list)["name"]
    cpu_pokemon_data = create_pokemon_data(get_pokemon_data(POKEMON_API_URL, cpu_pokemon_choice))
    print(f"\nCPU's Pokémon: {cpu_pokemon_data['name']}")
    print()


    # Start the game
    play_game(player_pokemon_data, cpu_pokemon_data)

if __name__ == "__main__":
    main()
