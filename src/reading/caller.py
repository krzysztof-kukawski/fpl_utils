"""
FPL api caller
"""

import json

import requests
from requests import Response

from src.reading.players import PlayerRoster


class FPLCaller:
    """
    FPL api caller class, gets names of players from a single url,
    then gets their per game week stats
    """

    def __init__(self, roster_class: type[PlayerRoster]) -> None:
        self._roster_class = roster_class
        self.roster: PlayerRoster

    def get_names_from_api(self, url: str) -> None:
        """

        :param url:
        :return:
        """
        data = self._get(url)

        self.roster = self._roster_class(data["elements"])

    def get_gw_history_from_api(self, url: str, gw: int) -> None:
        """

        :param url:
        :param gw:
        :return:
        """
        data = self._get(url)

        self.roster.extend_history(gw, data["elements"])

    def get_roster(self) -> PlayerRoster:
        """

        :return:
        """
        return self.roster

    @staticmethod
    def _get(url: str) -> dict:
        data: Response = requests.get(url, timeout=60)
        data_content: dict = json.loads(data.content)

        return data_content
