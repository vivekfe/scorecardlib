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

    def test_update_Score(self):
        leaderboard = Scoreboard()
        home_team = "Germany"
        away_team= "France"
        team_combination = f"{home_team}-{away_team}"
        leaderboard.start_game(home_team, away_team)
        self.assertEqual(leaderboard.games[team_combination].home_team, "Germany")
        self.assertEqual(leaderboard.games[team_combination].away_team, "France")
        leaderboard.update_score(home_team, away_team, 10, 5)
        self.assertEqual(leaderboard.games[team_combination].home_score, 10)
        self.assertEqual(leaderboard.games[team_combination].away_score, 5)

    def test_check_if_match_ongoing(self):
        # Test to check if any team exists
        leaderboard = Scoreboard()
        home_team = "Britain"
        away_team = "Isreal"
        with self.assertRaises(Exception) as context:
            leaderboard.update_score(home_team, away_team, 10, 5)

        self.assertTrue(f"There is no ongoing game between {home_team} and {away_team}\n" in str(context.exception))