def generate_fixtures(teams):
    fixtures = []

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            print(teams[i]["name"], "vs", teams[j]["name"])

    return fixtures