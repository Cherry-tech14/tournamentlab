import json

def save_tournament(teams, fixtures, filename):
    data = {
        "teams": teams,
        "fixtures": fixtures
    }

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_tournament(filename):
    with open(filename, "r") as file:
        data = json.load(file)

    return data