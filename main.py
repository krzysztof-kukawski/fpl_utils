import json

import requests

from players import PlayerRoster, Player


def find_by_id(players: PlayerRoster, pl_id: int) -> Player:
    for player in players:
        if player.id == pl_id:
            return player


data = requests.get('https://fantasy.premierleague.com/api/bootstrap-static/')
data = json.loads(data.content)

roster = PlayerRoster(data['elements'])

for gw in range(1, 22):
    gw_data = requests.get(f'https://fantasy.premierleague.com/api/event/{gw}/live/')
    gw_data = json.loads(gw_data.content)

    for elem in gw_data['elements']:
        points = elem['stats']['total_points']
        play_id = elem['id']
        pl = find_by_id(roster, play_id)
        pl.add_points(gw, points)

for p in roster:
    print(p.name, p.points)
