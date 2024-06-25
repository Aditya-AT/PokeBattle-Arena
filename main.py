import random
import pokemon
import generate_teams
import battle

def main():
    # Create two teams
    team_red = generate_teams.generate_team('Ash', 'Team Red')
    team_blue = generate_teams.generate_team('Gary', 'Team Blue')

    # Check if teams are created successfully
    if not team_red or not team_blue:
        print("Failed to create teams. Exiting...")
        return

    # Display the teams
    print("Team Red:")
    for poke in team_red:
        print(poke)
    print("\nTeam Blue:")
    for poke in team_blue:
        print(poke)

    # Start the battle
    print("\nBattle Begins!")
    battle.simulate_battle(team_red, team_blue)

    # Determine and display the winning team
    red_alive = any(p.hp > 0 for p in team_red)
    blue_alive = any(p.hp > 0 for p in team_blue)

    if red_alive and not blue_alive:
        print("Team Red wins!")
    elif blue_alive and not red_alive:
        print("Team Blue wins!")
    else:
        print("It's a tie!")

if __name__ == '__main__':
    main()
