def register_team(teams, name):
    name = name.strip()

    if len (name) < 2 or len(name) > 30:
        raise ValueError("Team name must contain 2 to 30 characters")

    for names in teams:
        if name.casefold() == names["name"].casefold():
            raise ValueError("Team already exist")

    team_number = len(teams) + 1

    team_id = f"TM{team_number:03d}"

    team = {
        "id": team_id,
        "name": name
    }

    teams.append(team)
