import unittest

from src.players import Player, PlayerRoster


class PlayerTest(unittest.TestCase):
    def test_extend_history(self):
        test_player = Player(9, "test_player")
        test_player.extend_history(11, 8)
        test_player.extend_history(1, 3)

        actual = [{"gw": 11, "points": 8}, {"gw": 1, "points": 3}]
        self.assertEqual(test_player.history, actual)


class PlayerRosterTest(unittest.TestCase):

    def test_roster(self):
        test_data = [
            {"id": 121, "web_name": "test_player1"},
            {"id": 31, "web_name": "test_player2"},
        ]
        test_roster = PlayerRoster(test_data)

        test_players = [player for player in test_roster]

        self.assertEqual(test_players[0].name, "test_player1")
        self.assertEqual(test_players[1].name, "test_player2")
        self.assertEqual(test_players[0].id, 121)
        self.assertEqual(test_players[1].id, 31)


if __name__ == "__main__":
    unittest.main()
