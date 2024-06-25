import random

# Constants for type effectiveness
TYPE_TABLE = {'normal': {'normal': 1, 'fire': 1 , 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                         'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 0,
                         'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1},
              'fire': {'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 1, 'grass': 2, 'ice': 2, 'fighting': 1,
                       'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 2, 'rock': 0.5, 'ghost': 1,
                       'dragon': 0.5, 'dark': 1, 'steel': 2, 'fairy': 1},
              'water': {'normal': 1, 'fire': 2, 'water': 0.5, 'electric': 1, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                        'poison': 1, 'ground': 2, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1,
                        'dragon': 0.5, 'dark': 1, 'steel': 1, 'fairy': 1},
              'electric': {'normal': 1, 'fire': 1, 'water': 2, 'electric': 0.5, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                           'poison': 1, 'ground': 0, 'flying': 2, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                           'dragon': 0.5, 'dark': 1, 'steel': 1, 'fairy': 1},
              'grass': {'normal': 1, 'fire': 0.5, 'water': 2, 'electric': 1, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                        'poison': 0.5, 'ground': 2, 'flying': 0.5, 'psychic': 1, 'bug': 0.5, 'rock': 2, 'ghost': 1,
                        'dragon': 0.5, 'dark': 1, 'steel': 0.5, 'fairy': 1},
              'ice': {'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 1, 'grass': 2, 'ice': 0.5, 'fighting': 1,
                      'poison': 1, 'ground': 2, 'flying': 2, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1,
                      'dragon': 2, 'dark': 1, 'steel': 0.5, 'fairy': 1},
              'fighting': {'normal': 2, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 2, 'fighting': 1,
                           'poison': 0.5, 'ground': 1, 'flying': 0.5, 'psychic': 0.5, 'bug': 1, 'rock': 2, 'ghost': 0,
                           'dragon': 1, 'dark': 2, 'steel': 2, 'fairy': 0.5},
              'poison': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 2, 'ice': 1, 'fighting': 1,
                         'poison': 0.5, 'ground': 0.5, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 0.5,
                         'dragon': 1, 'dark': 1, 'steel': 0, 'fairy': 2},
              'ground': {'normal': 1, 'fire': 2, 'water': 1, 'electric': 2, 'grass': 0.5, 'ice': 1, 'fighting': 1,
                         'poison': 2, 'ground': 1, 'flying': 0, 'psychic': 1, 'bug': 0.5, 'rock': 2, 'ghost': 1,
                         'dragon': 1, 'dark': 1, 'steel': 2, 'fairy': 1},
              'flying': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 0.5, 'grass': 2, 'ice': 1, 'fighting': 2,
                         'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 0.5, 'ghost': 1,
                         'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1},
              'psychic': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 2,
                          'poison': 2, 'ground': 1, 'flying': 1, 'psychic': 0.5, 'bug': 1, 'rock': 1, 'ghost': 1,
                          'dragon': 1, 'dark': 0, 'steel': 0.5, 'fairy': 1},
              'bug': {'normal': 1, 'fire': 0.5, 'water': 1, 'electric': 1, 'grass': 2, 'ice': 1, 'fighting': 0.5,
                      'poison': 0.5, 'ground': 1, 'flying': 0.5, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 0.5,
                      'dragon': 1, 'dark': 2, 'steel': 0.5, 'fairy': 1},
              'rock': {'normal': 1, 'fire': 2, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 2, 'fighting': 0.5,
                       'poison': 1, 'ground': 0.5, 'flying': 2, 'psychic': 1, 'bug': 2, 'rock': 1, 'ghost': 1,
                       'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 1},
              'ghost': {'normal': 0, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                        'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 2,
                        'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 1},
              'dragon': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                         'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                         'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 0},
              'dark': {'normal': 1, 'fire': 1, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 1,
                       'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 2, 'bug': 1, 'rock': 1, 'ghost': 0.5,
                       'dragon': 1, 'dark': 0.5, 'steel': 1, 'fairy': 0.5},
              'steel': {'normal': 1, 'fire': 0.5, 'water': 0.5, 'electric': 0.5, 'grass': 1, 'ice': 2, 'fighting': 1,
                        'poison': 1, 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 2, 'ghost': 1,
                        'dragon': 1, 'dark': 1, 'steel': 0.5, 'fairy': 2},
              'fairy': {'normal': 1, 'fire': 0.5, 'water': 1, 'electric': 1, 'grass': 1, 'ice': 1, 'fighting': 2,
                        'poison': 0.5 , 'ground': 1, 'flying': 1, 'psychic': 1, 'bug': 1, 'rock': 1, 'ghost': 1,
                        'dragon': 2, 'dark': 2, 'steel':0.5 , 'fairy': 1}
              }



def calculate_type_effectiveness(attack_type, defender_types):
    """Calculates the overall type effectiveness of an attack against potentially dual-typed Pokémon."""
    effectiveness = 1.0
    for defender_type in defender_types:
        effectiveness *= TYPE_TABLE.get(attack_type, {}).get(defender_type, 1)
    return effectiveness

def calculate_damage(attack_type, defender):
    """Calculates the damage from an attack type to a defender considering the defender's dual types."""
    base_damage = random.randint(3, 11) - defender.defense
    type_effectiveness = calculate_type_effectiveness(attack_type, defender.types)
    adjusted_damage = base_damage * type_effectiveness
    final_damage = max(1, int(adjusted_damage + random.randint(-2, 5)))  # Ensure minimum damage is 1
    return final_damage

def battle_round(attacker, defender):
    """Conducts a single round of battle between two Pokémon."""
    attack_type = attacker.types[0]  # Using the first type as the move type
    damage = calculate_damage(attack_type, defender)
    defender.hp -= damage
    print(f"{attacker.name} attacks with {attack_type} type. Deals {damage} damage to {defender.name}. {defender.name} has {defender.hp} HP left.")
    if defender.hp <= 0:
        print(f"{defender.name} has fainted!")

def check_team_alive(team):
    """Check if any Pokémon in the team is still alive."""
    return any(p.hp > 0 for p in team)

def choose_next_pokemon(team, opposing_pokemon):
    """Choose the next Pokémon based on type advantage."""
    alive_pokemon = [p for p in team if p.hp > 0]
    if not alive_pokemon:
        return None
    if not opposing_pokemon:
        return random.choice(alive_pokemon)

    # Choose the Pokémon with type advantage
    best_choice = None
    best_effectiveness = 0
    for p in alive_pokemon:
        effectiveness = calculate_type_effectiveness(p.types[0], opposing_pokemon.types)
        if effectiveness > best_effectiveness:
            best_choice = p
            best_effectiveness = effectiveness
    return best_choice if best_choice else random.choice(alive_pokemon)

def simulate_battle(trainer_one, team_one, trainer_two, team_two):
    """Simulates a battle between two teams of Pokémon, handling different team sizes."""
    round_number = 1
    team_one_pokemon = choose_next_pokemon(team_one, None)
    team_two_pokemon = choose_next_pokemon(team_two, None)

    while check_team_alive(team_one) and check_team_alive(team_two):
        print(f"\n--- Round {round_number} ---")
        print(f"{team_one_pokemon.name} ({trainer_one}'s Team) vs {team_two_pokemon.name} ({trainer_two}'s Team)")

        if team_one_pokemon.speed > team_two_pokemon.speed:
            battle_round(team_one_pokemon, team_two_pokemon)
            if team_two_pokemon.hp > 0:
                battle_round(team_two_pokemon, team_one_pokemon)
        else:
            battle_round(team_two_pokemon, team_one_pokemon)
            if team_one_pokemon.hp > 0:
                battle_round(team_one_pokemon, team_two_pokemon)

        if team_two_pokemon.hp <= 0:
            team_two_pokemon = choose_next_pokemon(team_two, team_one_pokemon)
        if team_one_pokemon.hp <= 0:
            team_one_pokemon = choose_next_pokemon(team_one, team_two_pokemon)

        if not team_one_pokemon or not team_two_pokemon:
            break

        round_number += 1

        # Prompt for next round
        input("\nPress Enter to continue to the next round...")

    if check_team_alive(team_one):
        print(f"\n{trainer_one}'s team wins!")
    elif check_team_alive(team_two):
        print(f"\n{trainer_two}'s team wins!")
    else:
        print("\nIt's a tie!")

