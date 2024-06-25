# PokeBattle Arena

This Pokémon Battle Simulation project is a simplified version of Pokémon battles, designed to simulate battles between teams of Pokémon based on their types, stats, and speed. The project includes team generation, type effectiveness calculation, and a turn-based battle system.

## Features

- **Team Generation**: Create teams of Pokémon with types based on trainer preferences.
- **Type Effectiveness Calculation**: Calculate damage based on the type of the attack and the types of the defender.
- **Turn-Based Battle System**: Simulate turn-based battles between two teams of Pokémon, with each round clearly separated.
- **Type-Based Pokémon Selection**: Select the next Pokémon to battle based on type advantages to ensure a fair fight.
- **User Prompts**: Prompts the user to continue to the next round after each battle, enhancing interactivity.

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Aditya-AT/PokeBattle-Arena.git
    cd PokeBattle-Arena
    ```

2. **Install Dependencies**

   This project doesn't have any external dependencies, but ensure you have Python installed (preferably version 3.6 or higher).

3. **Create the `names.txt` File**

   Create a file named `names.txt` with the following content:

    ```
    name,type1,type2
    Bulbasaur,Grass,Poison
    Ivysaur,Grass,Poison
    Venusaur,Grass,Poison
    Charmander,Fire,
    Charmeleon,Fire,
    Charizard,Fire,Flying
    Squirtle,Water,
    Wartortle,Water,
    Blastoise,Water,
    Caterpie,Bug,
    Metapod,Bug,
    Butterfree,Bug,Flying
    ```

## Usage

1. **Generate Teams**

   The teams are generated based on trainer preferences. You can specify trainers and their team names in the `main.py` file.

    ```python
    # Example team generation
    team_one = generate_team('Ash', 'Team Red')
    team_two = generate_team('Gary', 'Team Blue')
    ```

2. **Simulate the Battle**

   The main battle simulation is initiated by calling the `simulate_battle` function with the generated teams.

    ```python
    simulate_battle(team_one, team_two)
    ```

3. **Run the Simulation**

   Run the `main.py` script to start the simulation.

    ```bash
    python main.py
    ```

## Example

Here's an example of what the output might look like:

```plaintext
--- Round 1 ---
Charizard (Team One) vs Blastoise (Team Two)
Charizard attacks with Fire type. Deals 10 damage to Blastoise. Blastoise has 30 HP left.
Blastoise attacks with Water type. Deals 8 damage to Charizard. Charizard has 32 HP left.

Press Enter to continue to the next round...

--- Round 2 ---
Charizard (Team One) vs Blastoise (Team Two)
Charizard attacks with Fire type. Deals 12 damage to Blastoise. Blastoise has 18 HP left.
Blastoise attacks with Water type. Deals 10 damage to Charizard. Charizard has 22 HP left.

Press Enter to continue to the next round...

...

Team One wins!
