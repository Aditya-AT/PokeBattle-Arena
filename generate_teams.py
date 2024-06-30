import random
import pokemon

def generate_team(trainer: str, team_name: str) -> list:
    """
    Generates a team of six Pokémon for a given trainer, with team composition based on the trainer's preferences.

    Args:
    trainer (str): Name of the trainer.
    team_name (str): Designated name for the team.

    Returns:
    list: A list of six Pokémon objects.
    """
    trainer_preferences = {
        'Misty': ['water', 'fairy'],
        'Brock': ['rock', 'ground', 'fighting'],
        'Ash': ['electric', 'normal', 'fire', 'water', 'grass', 'flying', 'bug'],
        'Team Rocket': ['poison', 'dark', 'psychic'],
        'Gary': ['dragon', 'fire', 'steel', 'ground', 'flying']
    }

    team_name = f"team {team_name}"
    team = []

    # Determine trainer's preferred types, default to random if not listed
    preferred_types = trainer_preferences.get(trainer, [])
    preferred_types = set(pt.lower() for pt in preferred_types)  # Normalize to lowercase for comparison

    try:
        with open('names.txt', 'r') as f:
            next(f)  # Skip the header
            pokemon_entries = [line.strip().split(',') for line in f]
    except FileNotFoundError:
        print("Error: The file 'names.txt' was not found.")
        return []

    # Print debug information
    print("Trainer:", trainer)
    print("Preferred Types:", preferred_types)
    print("Pokémon Entries:", pokemon_entries)

    # Filter names based on preferred types if specific preferences are defined
    if preferred_types:
        filtered_entries = [entry for entry in pokemon_entries if any(pt.lower() in preferred_types for pt in entry[1:3] if pt)]
        selected_entries = random.sample(filtered_entries, k=6) if len(filtered_entries) >= 6 else filtered_entries
    else:
        # Select random names from the list, avoiding duplicates
        selected_entries = random.sample(pokemon_entries, k=6) if len(pokemon_entries) >= 6 else pokemon_entries

    # Print debug information
    print("Filtered Entries:", filtered_entries)
    print("Selected Entries:", selected_entries)

    # Create Pokémon instances from the selected entries
    for entry in selected_entries:
        name = entry[0]
        types = [t for t in entry[1:] if t]  # Filter out empty strings to avoid passing empty types
        team.append(pokemon.Pokemon(name, types))

    return team

def generate_custom_team(trainer: str, pokemon_list: list) -> list:
    """
    Generates a custom team of Pokémon for a given trainer based on user input.

    Args:
    trainer (str): Name of the trainer.
    pokemon_list (list): List of Pokémon names.

    Returns:
    list: A list of Pokémon objects.
    """
    team = []

    try:
        with open('names.txt', 'r') as f:
            next(f)  # Skip the header
            pokemon_entries = {line.strip().split(',')[0]: line.strip().split(',')[1:] for line in f}
    except FileNotFoundError:
        print("Error: The file 'names.txt' was not found.")
        return []

    for name in pokemon_list:
        if name in pokemon_entries:
            types = [t for t in pokemon_entries[name] if t]
            team.append(pokemon.Pokemon(name, types))
        else:
            print(f"Warning: {name} is not found in names.txt and will be skipped.")

    return team
