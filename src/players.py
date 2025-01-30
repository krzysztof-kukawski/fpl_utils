"""players module"""

from typing import Iterator

import pandas as pd


class Player:
    """
    FPL player class
    """
    def __init__(self, player_id: int, name: str) -> None:
        self.id = player_id
        self.name = name
        self.history = []

    def extend_history(self, gw: int, points: int) -> None:
        """
        Add a particular gameweek to player's history
        :param gw:
        :param points:
        :return:
        """
        gw_stats = {"gw": gw, "points": points}

        self.history.append(gw_stats)

    def to_dataframe(self):
        """

        :return: pd.DataFrame
            player's history in DataFrame format
        """
        return pd.DataFrame(self.history)


class PlayerRoster:
    """
    Collection class for storing players
    """
    def __init__(self, elem_data: list[dict]) -> None:
        self.players = []
        for elem in elem_data:
            player = Player(elem["id"], elem["web_name"])
            self.players.append(player)

    def __iter__(self) -> Iterator[Player]:
        yield from self.players
