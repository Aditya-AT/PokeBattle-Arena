# import argparse
# import generate_teams
# import battle
#
# def parse_custom_pokemons(custom_pokemon_str):
#     custom_pokemons = []
#     for entry in custom_pokemon_str.split(';'):
#         parts = entry.split(',')
#         name = parts[0]
#         types = parts[1:]
#         custom_pokemons.append([name] + types)
#     return custom_pokemons
#
# def main():
#     parser = argparse.ArgumentParser(description="Pokémon Battle Simulation")
#     parser.add_argument("--trainer1", type=str, default="Ash", help="Name of the first trainer")
#     parser.add_argument("--trainer2", type=str, default="Gary", help="Name of the second trainer")
#     parser.add_argument("--team1", type=str, help="Custom Pokémon for the first trainer (format: name,type1,type2;name,type1,type2;...)")
#     parser.add_argument("--team2", type=str, help="Custom Pokémon for the second trainer (format: name,type1,type2;name,type1,type2;...)")
#
#     args = parser.parse_args()
#
#     # Create two teams
#     team_one = generate_teams.generate_team(args.trainer1, 'Team Red', parse_custom_pokemons(args.team1) if args.team1 else None)
#     team_two = generate_teams.generate_team(args.trainer2, 'Team Blue', parse_custom_pokemons(args.team2) if args.team2 else None)
#
#     # Check if teams are created successfully
#     if not team_one or not team_two:
#         print("Failed to create teams. Exiting...")
#         return
#
#     # Display the teams
#     print(f"{args.trainer1}'s Team:")
#     for poke in team_one:
#         print(poke)
#     print(f"\n{args.trainer2}'s Team:")
#     for poke in team_two:
#         print(poke)
#
#     # Start the battle
#     print("\nBattle Begins!")
#     battle.simulate_battle(args.trainer1, team_one, args.trainer2, team_two)
#
# if __name__ == '__main__':
#     main()

import random
import argparse
import pokemon
import generate_teams
import battle

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Pokémon Battle Simulation")
    parser.add_argument('--trainer1', type=str, default='Ash', help='Name of the first trainer')
    parser.add_argument('--trainer2', type=str, default='Gary', help='Name of the second trainer')
    parser.add_argument('--custom1', type=str, help='Comma-separated list of Pokémon names for the first trainer')
    parser.add_argument('--custom2', type=str, help='Comma-separated list of Pokémon names for the second trainer')
    args = parser.parse_args()

    # Create two teams
    if args.custom1:
        team_one = generate_teams.generate_custom_team(args.trainer1, args.custom1.split(','))
    else:
        team_one = generate_teams.generate_team(args.trainer1, 'Team Red')

    if args.custom2:
        team_two = generate_teams.generate_custom_team(args.trainer2, args.custom2.split(','))
    else:
        team_two = generate_teams.generate_team(args.trainer2, 'Team Blue')

    # Check if teams are created successfully
    if not team_one or not team_two:
        print("Failed to create teams. Exiting...")
        return

    # Display the teams
    print(f"{args.trainer1}'s Team:")
    for poke in team_one:
        print(poke)
    print(f"\n{args.trainer2}'s Team:")
    for poke in team_two:
        print(poke)

    # Start the battle
    print("\nBattle Begins!")
    battle.simulate_battle(args.trainer1, team_one, args.trainer2, team_two)

if __name__ == '__main__':
    main()
