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

    try:
        with open('names.txt', 'r') as f:
            next(f)  # Skip the header
            pokemon_entries = [line.strip().split(',') for line in f]
    except FileNotFoundError:
        print("Error: The file 'names.txt' was not found.")
        return []

    if preferred_types:
        # Normalize preferred types to lower case for case-insensitive comparison
        preferred_types = set(pt.lower() for pt in preferred_types)

        # Filter entries where any of the Pokémon's types match the preferred types
        filtered_entries = [
            entry for entry in pokemon_entries
            if set(pt.lower() for pt in entry[1:3] if pt).intersection(preferred_types)
        ]
        selected_entries = random.sample(filtered_entries, k=6) if len(filtered_entries) >= 6 else filtered_entries
    else:
        # Select random names from the list, avoiding duplicates
        selected_entries = random.sample(pokemon_entries, k=6) if len(pokemon_entries) >= 6 else pokemon_entries

    # Create Pokémon instances from the selected entries
    for entry in selected_entries:
        name = entry[0]
        types = [t for t in entry[1:] if t]  # Filter out empty strings to avoid passing empty types
        team.append(pokemon.Pokemon(name, types))

    return team
