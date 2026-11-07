from tournament.teams import register_team

from tournament.fixtures import generate_fixtures, record_score

teams = []

while len(teams) < 4:
    name = input("Enter team name: ")

    try:
        register_team(teams, name)

    except ValueError as error:
        print(error)

#print(teams)

fixtures = generate_fixtures(teams)
record_score(fixtures, 1, 3, 1)
print(fixtures[0])
print(fixtures)
