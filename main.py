import random
import pokemon
import generate_teams
import battle

def main():
    # Define trainer names
    trainer_one = 'Ash'
    trainer_two = 'Gary'

    # Create two teams
    team_one = generate_teams.generate_team(trainer_one, 'Team Red')
    team_two = generate_teams.generate_team(trainer_two, 'Team Blue')

    # Check if teams are created successfully
    if not team_one or not team_two:
        print("Failed to create teams. Exiting...")
        return

    # Display the teams
    print(f"{trainer_one}'s Team:")
    for poke in team_one:
        print(poke)
    print(f"\n{trainer_two}'s Team:")
    for poke in team_two:
        print(poke)

    # Start the battle
    print("\nBattle Begins!")
    battle.simulate_battle(trainer_one, team_one, trainer_two, team_two)

if __name__ == '__main__':
    main()