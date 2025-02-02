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
        self.history: list[dict] = []

    def extend_history(self, gw: int, stats: dict) -> None:
        """
        Add a particular game week to player's history
        :param stats:
        :param gw:
        :return:
        """
        gw_stats = {"gw": gw, "stats": stats}

        self.history.append(gw_stats)

    def to_dataframe(self) -> pd.DataFrame:
        """

        :return: pd.DataFrame
            player's history in DataFrame format
        """
        df = pd.DataFrame()
        for i in self.history:
            new_df = pd.DataFrame(i['stats'], index=[i['gw']])
            df = pd.concat([df, new_df])

        df['name'] = self.name
        df['id'] = self.id
        return df


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

    def __len__(self) -> int:
        return len(self.players)

    def find_by_id(self, player_id: int) -> Player | None:
        """

        :param player_id:
        :return:
        """
        for player in self:
            if player.id == player_id:
                return player

        return None

    def find_by_name(self, name: str) -> Player | None:
        """

        :param name:
        :return:
        """
        for player in self:
            if player.name == name:
                return player

        return None

    def extend_history(self, gw: int, gw_stats: list[dict]) -> None:
        """

        :param gw:
        :param gw_stats:
        :return:
        """
        for player_stats in gw_stats:
            player_id = player_stats['id']
            player = self.find_by_id(player_id)
            if player:
                stats = player_stats['stats']
                player.extend_history(gw, stats)
