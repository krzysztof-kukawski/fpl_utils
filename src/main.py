"""
main script
"""

from src.reading.caller import FPLCaller
from src.reading.players import PlayerRoster

caller = FPLCaller(PlayerRoster)
caller.get_names_from_api("https://fantasy.premierleague.com/api/bootstrap-static/")

for gw in range(1, 24):
    caller.get_gw_history_from_api(
        f"https://fantasy.premierleague.com/api/event/{gw}/live/", gw
    )

roster = caller.get_roster()

for player in roster:
    player.to_dataframe().to_csv(f"data/{player.name}.csv")
