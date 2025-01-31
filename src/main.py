"""
main script
"""
import json

import requests

from src.players import PlayerRoster

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

    roster.extend_history(gw, gw_data["elements"])

for player in roster:
    print(player.name, player.history)
