import unittest

import pandas as pd
from pandas.testing import assert_frame_equal

from src.players import Player, PlayerRoster


class PlayerTest(unittest.TestCase):
    def test_extend_history(self):
        test_player = Player(9, "test_player")
        test_player.extend_history(11, 8)
        test_player.extend_history(1, 3)

        actual = [{"gw": 11, "points": 8}, {"gw": 1, "points": 3}]
        self.assertEqual(test_player.history, actual)

    def test_to_dataframe(self):
        test_player = Player(9, "test_player")
        test_player.extend_history(11, 8)
        test_player.extend_history(1, 3)

        player_frame = test_player.to_dataframe()
        test_frame = pd.DataFrame([{"gw": 11, "points": 8}, {"gw": 1, "points": 3}])

        assert_frame_equal(player_frame, test_frame)


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

    def test_find_by_id(self):
        test_data = [
            {"id": 121, "web_name": "test_player1"},
            {"id": 31, "web_name": "test_player2"},
        ]
        test_roster = PlayerRoster(test_data)

        test_player = {"id": 121, "name": "test_player1"}
        found_player = test_roster.find_by_id(121)
        found_player = {"id": found_player.id, "name": found_player.name}

        not_found = test_roster.find_by_id(132)

        self.assertEqual(found_player, test_player)
        self.assertEqual(not_found, None)

    def test_extend_history(self):
        gw1 = [
            {'id': 721, 'stats': {'total_points': 3}},
            {'id': 722, 'stats': {'total_points': 0}}]
        gw2 = [
            {'id': 721, 'stats': {'total_points': 1}},
            {'id': 722, 'stats': {'total_points': 9}}]

        extended_hist_1 = [{"gw": 1, "points": 3}, {"gw": 2, "points": 1}]
        extended_hist_2 = [{"gw": 1, "points": 0}, {"gw": 2, "points": 9}]

        test_players = [
            {"id": 721, "web_name": "test_player1"},
            {"id": 722, "web_name": "test_player2"},
        ]
        test_roster = PlayerRoster(test_players)
        test_roster.extend_history(1, gw1)
        test_roster.extend_history(2, gw2)

        player1 = test_roster.find_by_id(721)
        player2 = test_roster.find_by_id(722)

        self.assertEqual(player1.history, extended_hist_1)
        self.assertEqual(player2.history, extended_hist_2)

        if __name__ == "__main__":
            unittest.main()
