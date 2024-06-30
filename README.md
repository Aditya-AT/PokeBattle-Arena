# PokeBattle Arena
![alt text](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ0ELb1h1uAMhPuoA3flKMxKUkUd4-i1NNrfw&s)

This Pokémon Battle Simulation project is a simplified version of Pokémon battles, designed to simulate battles between teams of Pokémon based on their types, stats, and speed. The project includes team generation, type effectiveness calculation, and a turn-based battle system.

## Features

- **Team Generation**: Create teams of Pokémon with types based on trainer preferences.
- **Custom Trainer and Team**: Create custom trainers and specify custom Pokémon teams via command-line input.
- **Type Effectiveness Calculation**: Calculate damage based on the type of the attack and the types of the defender.
- **Turn-Based Battle System**: Simulate turn-based battles between two teams of Pokémon, with each round clearly separated.
- **Type-Based Pokémon Selection**: Select the next Pokémon to battle based on type advantages to ensure a fair fight.
- **User Prompts**: Prompts the user to continue to the next round after each battle, enhancing interactivity.

## Concepts Learned

Through this project, several important programming and software development concepts were applied and reinforced, including:

- **Object-Oriented Programming (OOP)**: Utilizing classes and objects to model Pokémon, their attributes, and behaviors.
- **File I/O**: Reading and writing files to manage Pokémon data.
- **Randomness and Probabilities**: Using randomization to simulate realistic and unpredictable battles.
- **Conditional Logic**: Implementing game rules and mechanics through conditional statements.
- **Modular Programming**: Breaking down the program into modular functions and classes for better organization and maintainability.
- **Type Handling and Effectiveness**: Managing complex interactions between different Pokémon types to accurately simulate battle mechanics.
- **User Interaction**: Creating a user-friendly interface through prompts and clear output formatting.
- **Algorithm Design**: Designing algorithms for damage calculation, Pokémon selection, and battle simulation.

## Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Aditya-AT/PokeBattle-Arena.git
    cd PokeBattle-Arena
    ```

2. **Install Dependencies**

   This project doesn't have any external dependencies, but ensure you have Python installed (preferably version 3.6 or higher).

## Usage

1. **Generate Teams**

   The teams are generated based on trainer preferences. You can specify trainers and their team names in the `main.py` file or via command-line input.

    ```python
    # Example team generation
    team_one = generate_team('Ash', 'Team Red')
    team_two = generate_team('Gary', 'Team Blue')
    ```

2. **Custom Trainer and Team**

   You can create custom trainers and specify a custom list of Pokémon via command-line input.

    ```bash
    python main.py --trainer1 "CustomTrainer1" --custom1 "Bulbasaur,Charmander,Squirtle" --trainer2 "CustomTrainer2" --custom2 "Caterpie,Metapod,Butterfree"
    ```

3. **Simulate the Battle**

   The main battle simulation is initiated by calling the `simulate_battle` function with the generated teams.

    ```python
    simulate_battle(trainer_one, team_one, trainer_two, team_two)
    ```

4. **Run the Simulation**

   Run the `main.py` script to start the simulation.

    ```bash
    python main.py
    ```

## Example

Here's an example of what the output might look like:

```plaintext
--- Round 1 ---
Charizard (Ash's team) vs Blastoise (Gary's Team)
Charizard attacks with Fire type. Deals 10 damage to Blastoise. Blastoise has 30 HP left.
Blastoise attacks with Water type. Deals 8 damage to Charizard. Charizard has 32 HP left.

Press Enter to continue to the next round...

--- Round 2 ---
Charizard (Ash's team) vs Blastoise (Gary's Team)
Charizard attacks with Fire type. Deals 12 damage to Blastoise. Blastoise has 18 HP left.
Blastoise attacks with Water type. Deals 10 damage to Charizard. Charizard has 22 HP left.

Press Enter to continue to the next round...

...

Team One wins!
```


![alt text](https://static1.cbrimages.com/wordpress/wp-content/uploads/2020/10/Ashs-Strongest-Pok--mon-From-Season-1-Ranked-featured-image.jpg)


## Future Improvements
1. **Advanced Move Selection**: Implementing a more sophisticated move selection mechanism for Pokémon.
2. **Graphical Interface**: Developing a graphical user interface for the battle simulation.

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request with your improvements. Contributions are welcome!

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
Pokémon names and types are trademarks of Nintendo, Game Freak, and The Pokémon Company.
Any third-party images or content used in this project are the property of their respective owners and are used here for educational purposes under fair use.
