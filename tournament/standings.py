def calculate_standings(teams, fixtures):
    standings = {}

    for team in teams:
        standings[team["id"]] = {
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
                return "home team wins"

            elif match["home_score"] == match["away_score"]:
                return "both teams draw"

            else:
                return "away team wins"

            

    return standings