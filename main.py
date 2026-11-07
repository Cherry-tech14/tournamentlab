from tournament.teams import register_team

from tournament.fixtures import generate_fixtures

teams = []

while len(teams) < 4:
    name = input("Enter team name: ")

    try:
        register_team(teams, name)

    except ValueError as error:
        print(error)

print(teams)

generate_fixtures(teams)
