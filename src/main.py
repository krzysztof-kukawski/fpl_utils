"""
main script
"""
import json

import requests

from src.players import PlayerRoster, Player


def find_by_id(players: PlayerRoster, pl_id: int) -> Player | None:
    """

    :param players: PlayerRoster
    :param pl_id: int
    :return:
    """
    for player in players:
        if player.id == pl_id:
            return player
    return None


data = requests.get(
    "https://fantasy.premierleague.com/api/bootstrap-static/", timeout=60
)
data = json.loads(data.content)
print(type(data["elements"]))
roster = PlayerRoster(data["elements"])

for gw in range(1, 22):
    gw_data = requests.get(
        f"https://fantasy.premierleague.com/api/event/{gw}/live/", timeout=60
    )
    gw_data = json.loads(gw_data.content)

    for elem in gw_data["elements"]:
        points = elem["stats"]["total_points"]
        play_id = elem["id"]
        pl = find_by_id(roster, play_id)
        pl.extend_history(gw, points)

for p in roster:
    print(p.name, p.history)
