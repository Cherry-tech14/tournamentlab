def calculate_standings(teams, fixtures):
    standings = {}

    for team in teams:
        standings[team["id"]] = {
            "id": team["id"],
            "name": team["name"],
            "played": 0,
            "wins": 0,
            "draws": 0,
            "losses": 0,
            "goals_for": 0,
            "goals_against": 0,
            "goal_difference": 0,
            "points": 0
        }

    for match in fixtures:
        if match["home_score"] is not None and match["away_score"] is not None:
            standings[match["home_team"]]["played"] += 1
            standings[match["away_team"]]["played"] += 1

            standings[match["home_team"]]["goals_for"] += match["home_score"]
            standings[match["away_team"]]["goals_for"] += match["away_score"]

            standings[match["home_team"]]["goals_against"] += match["away_score"]
            standings[match["away_team"]]["goals_against"] += match["home_score"]

            if match["home_score"] > match["away_score"]:
                standings[match["home_team"]]["wins"] += 1
                standings[match["away_team"]]["losses"] += 1
                standings[match["home_team"]]["points"] += 3

                

            elif match["home_score"] == match["away_score"]:
                standings[match["home_team"]]["draws"] += 1
                standings[match["away_team"]]["draws"] += 1
                standings[match["home_team"]]["points"] += 1
                standings[match["away_team"]]["points"] += 1

            else:
                standings[match["away_team"]]["wins"] +=  1
                standings[match["home_team"]]["losses"] += 1
                standings[match["away_team"]]["points"] += 3

    for team in teams:
        standings[team["id"]]["goal_difference"] = standings[team["id"]]["goals_for"] - standings[team["id"]]["goals_against"]

    standings_list = list(standings.values())

    sorted_standings = sorted(
        standings_list,
        key=lambda team: (
            team["points"],
            team["goal_difference"],
            team["goals_for"]
        ),
        reverse=True
    )

    return sorted_standings

def get_champion(teams, fixtures):
    if not fixtures:
        return None

    for match in fixtures:
        if match["home_score"] is None or match["away_score"] is None:
            return None

    standings = calculate_standings(teams, fixtures)

    if not standings:
        return None

    champion = standings[0]

    return champion
