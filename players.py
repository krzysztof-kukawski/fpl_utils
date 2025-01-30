class PlayerRoster:
    def __init__(self, elem_data: dict):
        self.players = []
        for elem in elem_data:
            player = Player(elem['id'], elem['web_name'])
            self.players.append(player)

    def __iter__(self):
        for player in self.players:
            yield player


class Player:
    def __init__(self, player_id: int, name: str):
        self.id = player_id
        self.name = name
        self.points = {}

    def add_points(self, gw: int, points:int):
        self.points[gw] = points
