"""players module"""

from __future__ import annotations

from typing import Iterator, Any

import pandas as pd

from src.prediction.time_steps import TimeStepsTransformer


class Player:
    """
    FPL player class
    """

    def __init__(self, player_id: int, name: str) -> None:
        self.id = player_id
        self.name = name
        self.history: list[dict] = []

    @classmethod
    def from_csv(cls, path: str) -> Player:
        """

        :param path:
        :return:
        """
        raw_frame = pd.read_csv(path, index_col=0)
        history = []
        for i in range(1, raw_frame.shape[0] + 1):
            gw_stats: dict[str, Any] = {}
            stats = raw_frame.loc[i].to_dict()
            gw_stats.update({"gw": i})
            gw_stats.update({"stats": stats})
            history.append(gw_stats)

        name = history[0]["stats"]["name"]
        player_id = history[0]["stats"]["id"]

        player = cls(player_id, name)

        for gw in history:
            gw["stats"].pop("name")
            gw["stats"].pop("id")

            player.extend_history(gw["gw"], gw["stats"])

        return player

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
            new_df = pd.DataFrame(i["stats"], index=[i["gw"]])
            df = pd.concat([df, new_df])

        df["name"] = self.name
        df["id"] = self.id
        return df

    def to_time_steps(self, n_time_steps: int) -> pd.DataFrame:
        """

        :param n_time_steps:
        :return:
        """
        df = self.to_dataframe()
        transformer = TimeStepsTransformer(df)
        transformed = transformer.transform(n_time_steps)

        return transformed


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
            player_id = player_stats["id"]
            player = self.find_by_id(player_id)
            if player:
                stats = player_stats["stats"]
                player.extend_history(gw, stats)
