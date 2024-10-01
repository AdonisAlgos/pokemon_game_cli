# Pokémon Battle Game

## Overview
This is a command-line Pokémon battle game where the player selects a Pokémon, and the CPU randomly selects one as well. The game simulates a turn-based battle where the two Pokémon attack and defend in alternating rounds until one faints. The game retrieves Pokémon data from the PokéAPI.

## Features
- Choose a Pokémon from the API.
- Battle against a CPU-chosen Pokémon.
- Turn-based attacks based on random rolls and Pokémon stats.
- Simulated battle rounds with attack and defense checks.
- Game ends when one Pokémon's HP reaches zero.

## How to Play
1. Run the script in your Python environment.
2. A list of Pokémon will be displayed for you to choose from.
3. Type the name of the Pokémon you want to use.
4. The CPU will select a Pokémon at random.
5. The battle begins, and both the player and CPU take turns attacking and defending until one Pokémon faints.

## Code Structure

### Constants
- **`POKEMON_API_URL`**: The base URL for the Pokémon API.
- **`KEY_WIDTH`** & **`VALUE_WIDTH`**: Constants used for formatting the display of Pokémon stats.

### Functions

#### `get_pokemon_list(url)`
Fetches a list of available Pokémon from the provided API URL.

- **Parameters**: 
  - `url` (string): API endpoint.
- **Returns**: 
  - A list of Pokémon names.

#### `get_pokemon_data(url, pokemon)`
Retrieves detailed data for a specific Pokémon from the API.

- **Parameters**:
  - `url` (string): API base URL.
  - `pokemon` (string): Name of the Pokémon.
- **Returns**: 
  - JSON data containing the Pokémon’s attributes.

#### `create_pokemon_data(data)`
Processes raw Pokémon data to extract and format key attributes such as name, ability, height, weight, and stats.

- **Parameters**: 
  - `data` (JSON): The raw Pokémon data from the API.
- **Returns**: 
  - A dictionary containing the formatted Pokémon data.

#### `display_pokemon_list(pokemon_list)`
Displays the list of Pokémon names in a grid format.

- **Parameters**: 
  - `pokemon_list` (list): List of Pokémon names.
- **Returns**: 
  - None (prints output).

#### `display_pokemon_stats(pokemon_data)`
Displays the formatted stats of a selected Pokémon.

- **Parameters**: 
  - `pokemon_data` (dict): Formatted Pokémon data.
- **Returns**: 
  - None (prints output).

#### `play_game(player_pokemon_data, cpu_pokemon_data)`
Simulates the Pokémon battle game between the player’s Pokémon and the CPU’s Pokémon, managing turn-based attacks and defense.

- **Parameters**:
  - `player_pokemon_data` (dict): Formatted data for the player's Pokémon.
  - `cpu_pokemon_data` (dict): Formatted data for the CPU’s Pokémon.
- **Returns**: 
  - None (prints game progress and results).

### Main Function

#### `main()`
This is the main function that runs the game. It performs the following steps:
1. Fetches the list of Pokémon from the API.
2. Displays the list for the player to choose from.
3. Retrieves and displays the chosen Pokémon's stats.
4. Randomly selects a Pokémon for the CPU.
5. Starts the battle between the player and the CPU using the `play_game` function.

## Installation

1. Clone the repository or download the script.
2. Make sure you have Python installed.
3. Install the required packages by running:
   ```bash
   pip install requests
