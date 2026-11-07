def generate_fixtures(teams):
    fixtures = []

    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            
            match = {
                "home_team": teams[i]["id"],
                "away_team": teams[j]["id"],
                "home_score": None,
                "away_score": None
            }

            fixtures.append(match)

    return fixtures

def record_score(fixtures, match_number, home_score, away_score):

    if type(home_score) is not int:
        raise ValueError("Scores must be an integer")

    if type (away_score) is not int:
        raise ValueError("Scores must be an integer")

    if home_score < 0 or away_score < 0:
        raise ValueError("Scores cannot be negative")

    if type(match_number) is not int:
        raise ValueError("Match number must be an integer")

    if match_number < 1 or match_number > len(fixtures):
        raise ValueError("Invalid match number")

    match = fixtures[match_number - 1]

    match["home_score"] = home_score
    match["away_score"] = away_score

   