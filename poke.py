import requests
import json


# Function to get Pokémon data by name
def get_pokemon_by_name(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
    response = requests.get(url)

    if response.status_code == 200:  # Check if request was successful
        return json.loads(response.text)
    else:
        print(f"Pokémon '{pokemon_name}' not found!")
        return None


# Function to display Pokémon stats
def display_pokemon_stats(pokemon_data):
    if pokemon_data:  # If we successfully got the data
        print(f"\nPokémon: {pokemon_data['name'].capitalize()}")
        print("Stats:")

        for stat in pokemon_data['stats']:  # Iterating through each stat
            stat_name = stat['stat']['name']
            stat_value = stat['base_stat']
            print(f"{stat_name.capitalize()}: {stat_value}")
    else:
        print("No data to display.")


# Main Program
pokemon_name = input("Enter the name of the Pokémon: ")  # Ask the user for a Pokémon name
pokemon_data = get_pokemon_by_name(pokemon_name)  # Get the data
display_pokemon_stats(pokemon_data)  # Display the stats
