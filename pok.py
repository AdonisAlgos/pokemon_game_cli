import requests
import json
import random


# Function to get a list of Pokémon from the API
def get_pokemon_list():
    url = 'https://pokeapi.co/api/v2/pokemon/'  # Increase the limit to get more Pokémon
    response = requests.get(url)
    pokemon_list = json.loads(response.text)['results']

    print("List of Pokémon:")
    for pokemon in pokemon_list:
        print(pokemon['name'])
    return pokemon_list

# Function to get Pokémon data based on the chosen name
def get_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}/'
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Could not find Pokémon {pokemon_name}")
        return None
    return json.loads(response.text)


def display_pokemon_data(pokemon_data):
    name = pokemon_data['name'].capitalize()
    hp = pokemon_data['stats'][0]['base_stat']  # HP is the first stat
    attack = pokemon_data['stats'][1]['base_stat']  # Attack is the second stat
    defense = pokemon_data['stats'][2]['base_stat']  # Defense is the third stat
    speed = pokemon_data['stats'][5]['base_stat']  # Speed is the sixth stat
    ability = pokemon_data['abilities'][0]['ability']['name']  # First ability
    height = pokemon_data['height'] / 10  # Convert height to meters
    weight = pokemon_data['weight'] / 10  # Convert weight to kg

    print(f"--- {name} Stats ---")
    print(f"HP: {hp}")
    print(f"Attack: {attack}")
    print(f"Defense: {defense}")
    print(f"Speed: {speed}")
    print(f"Ability: {ability}")
    print(f"Height: {height}m")
    print(f"Weight: {weight}kg")

    return {
        'name': name,
        'hp': hp,
        'attack': attack,
        'defense': defense,
        'speed': speed
    }

# Function to assign a random Pokémon to the CPU
def assign_random_pokemon(pokemon_list):
    random_pokemon = random.choice(pokemon_list)['name']
    print(f"The CPU chose: {random_pokemon.capitalize()}")
    return random_pokemon


# Function to simulate a battle between user and CPU
def battle(user_pokemon_data, cpu_pokemon_data):
    print("--- Battle Start! ---")

    # Simple battle mechanics based on total stats
    user_hp = user_pokemon_data['hp']
    cpu_hp = cpu_pokemon_data['hp']

    # Battle loop until one Pokémon is defeated
    while user_hp > 0 and cpu_hp > 0:
        # User's turn to attack
        damage_to_cpu = max(1, user_pokemon_data['attack'] - cpu_pokemon_data['defense'] // 2)  # Basic damage formula
        cpu_hp -= damage_to_cpu
        print(f"{user_pokemon_data['name']} attacks {cpu_pokemon_data['name']} and deals {damage_to_cpu} damage.")
        print(f"{cpu_pokemon_data['name']}'s remaining HP: {max(0, cpu_hp)}")

        # Check if CPU is defeated
        if cpu_hp <= 0:
            print(f"\n{user_pokemon_data['name']} wins the battle!")
            break

        # CPU's turn to attack
        damage_to_user = max(1, cpu_pokemon_data['attack'] - user_pokemon_data['defense'] // 2)  # Basic damage formula
        user_hp -= damage_to_user
        print(f"{cpu_pokemon_data['name']} attacks {user_pokemon_data['name']} and deals {damage_to_user} damage.")
        print(f"{user_pokemon_data['name']}'s remaining HP: {max(0, user_hp)}")

        # Check if the user is defeated
        if user_hp <= 0:
            print(f"\n{cpu_pokemon_data['name']} wins the battle!")
            break

    print("\n--- Battle End! ---")
    # user_total_stats = (
    #         user_pokemon_data['hp'] +
    #         user_pokemon_data['attack'] +
    #         user_pokemon_data['defense'] +
    #         user_pokemon_data['speed']
    # )
    #
    # cpu_total_stats = (
    #         cpu_pokemon_data['hp'] +
    #         cpu_pokemon_data['attack'] +
    #         cpu_pokemon_data['defense'] +
    #         cpu_pokemon_data['speed']
    # )
    #
    # print(f"{user_pokemon_data['name']} vs {cpu_pokemon_data['name']}")
    # print(f"{user_pokemon_data['name']} total stats: {user_total_stats}")
    # print(f"{cpu_pokemon_data['name']} total stats: {cpu_total_stats}")
    #
    # if user_total_stats > cpu_total_stats:
    #     print(f"{user_pokemon_data['name']} wins!")
    # elif user_total_stats < cpu_total_stats:
    #     print(f"{cpu_pokemon_data['name']} wins!")
    # else:
    #     print("It's a draw!")


# Main program flow
def main():
    print("Welcome to the Pokémon battle game!")

    # Get the list of Pokémon and display them
    pokemon_list = get_pokemon_list()

    # Ask the user to choose a Pokémon
    user_choice = input("Enter your Pokémon (by name): ").lower()
    user_pokemon_data = get_pokemon_data(user_choice)

    if user_pokemon_data:
        # Display user's Pokémon stats
        user_stats = display_pokemon_data(user_pokemon_data)

        # Assign a random Pokémon to the CPU
        cpu_pokemon_name = assign_random_pokemon(pokemon_list)
        cpu_pokemon_data = get_pokemon_data(cpu_pokemon_name)

        if cpu_pokemon_data:
            # Display CPU's Pokémon stats
            cpu_stats = display_pokemon_data(cpu_pokemon_data)

            # Start the battle
            battle(user_stats, cpu_stats)
        else:
            print("Could not retrieve CPU Pokémon data.")
    else:
        print("Invalid Pokémon chosen, game over!")


# Run the main program
if __name__ == "__main__":
    main()
