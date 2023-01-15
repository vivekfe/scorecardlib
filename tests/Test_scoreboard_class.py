from unittest import TestCase
from scorecardlib.game import Game
from scorecardlib.scoreboard import Scoreboard

"""Sample table provided as an input and can be used for writing tests as well"""

# a. Mexico 0 - Canada 5
# b. Spain 10 - Brazil 2
# c. Germany 2 - France 2
# d. Uruguay 6 - Italy 6
# e. Argentina 3 - Australia 1


class TestScoreBoard(TestCase):
    def test_init_scoreboard(self):
        scoreboard = Scoreboard()
        self.assertEqual(scoreboard.games, dict())

    def test_start_game(self):
        leaderboard = Scoreboard()
        leaderboard.start_game("Germany", "France")
        self.assertEqual(leaderboard.games["Germany-France"].home_team, "Germany")
        self.assertEqual(leaderboard.games["Germany-France"].away_team, "France")
