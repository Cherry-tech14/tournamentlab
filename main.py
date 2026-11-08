from tournament.teams import register_team
from tournament.fixtures import generate_fixtures, record_score
from tournament.standings import calculate_standings, get_champion
from tournament.storage import save_tournament, load_tournament

def display_menu():
    print("\n===== TOURNAMENTLAB =====")
    print("1. Register Team")
    print("2. View Teams")
    print("3. Generate Fixtures")
    print("4. Record Match Results")
    print("5. View Standings")
    print("6. Announce Champion")
    print("7. Save Tournament")
    print("8. Load Tournament")
    print("9. Exit")

def main():
    teams = []
    fixtures = []

    while True:
        display_menu()

        choice = input("Choose an option: ").strip()

        if choice == "9":
            print("Goodbye")
            break

        elif choice == "1":
            if fixtures:
                print("Cannot register teams after fixtures are generated")
                continue

            elif len(teams) >= 8:
                print("Maximum of 8 teams allowed.")
                continue


            name = input("Enter team name: ").strip()
            
            try:
                team = register_team(teams, name)
                print(f"Team registered: {team['name']}")

            except ValueError as error:
                print(error)

        elif choice == "2":
            if not teams:
                print("No teams registered yet")

            else:
                for team in teams:
                    print(f"{team['id']} - {team['name']}")

        elif choice == "3":
            if len(teams) < 4:
                print("Atleast 4 teams are required")
            elif fixtures:
                print("Fixtures have already been generated")

            else:
                fixtures = generate_fixtures(teams)
                print("fixtures generated successfully")

if __name__ == "__main__":
    main()
