"""players module"""

from typing import Iterator


class Player:
    def __init__(self, player_id: int, name: str) -> None:
        self.id = player_id
        self.name = name
        self.history = []

    def extend_history(self, gw: int, points: int) -> None:
        gw_stats = {"gw": gw, "points": points}

        self.history.append(gw_stats)


class PlayerRoster:
    def __init__(self, elem_data: list[dict]) -> None:
        self.players = []
        for elem in elem_data:
            player = Player(elem["id"], elem["web_name"])
            self.players.append(player)

    def __iter__(self) -> Iterator[Player]:
        yield from self.players
