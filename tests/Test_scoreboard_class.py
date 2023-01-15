from unittest import TestCase
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
        away_team = "France"
        match_key = f"{home_team}-{away_team}"
        leaderboard.start_game(home_team, away_team)
        self.assertEqual(leaderboard.games[match_key].home_team, "Germany")
        self.assertEqual(leaderboard.games[match_key].away_team, "France")
        leaderboard.update_score(home_team, away_team, 10, 5)
        self.assertEqual(leaderboard.games[match_key].home_score, 10)
        self.assertEqual(leaderboard.games[match_key].away_score, 5)

    def test_check_if_match_ongoing(self):
        # Test to check if any team exists
        leaderboard = Scoreboard()
        home_team = "Britain"
        away_team = "Isreal"
        with self.assertRaises(Exception) as context:
            leaderboard.update_score(home_team, away_team, 10, 5)

        self.assertTrue(f"There is no ongoing game between {home_team} and {away_team}\n" in str(context.exception))

    def test_finish_game(self):
        leaderboard = Scoreboard()
        home_team = "Germany"
        away_team = "France"
        match_key = f"{home_team}-{away_team}"
        leaderboard.start_game(home_team, away_team)
        leaderboard.update_score(home_team, away_team, 2, 2)
        home_team_2 = "Spain"
        away_team_2 = "Brazil"
        match_key_2 = f"{home_team_2}-{away_team_2}"
        leaderboard.start_game(home_team_2, away_team_2)
        leaderboard.update_score(home_team, away_team, 10, 2)
        self.assertEqual(leaderboard.games[match_key].home_team, "Germany")
        self.assertEqual(leaderboard.games[match_key_2].home_team, "Spain")
        leaderboard.finish_game(home_team, away_team)
        self.assertNotIn(match_key, leaderboard.games.keys())

    def test_get_games_summary(self):
        """"We will first insert sample given games in leaderboard and then update their score"""
        # a. Mexico 0 - Canada 5
        # b. Spain 10 - Brazil 2
        # c. Germany 2 - France 2
        # d. Uruguay 6 - Italy 6
        # e. Argentina 3 - Australia 1
        leaderboard = Scoreboard()
        leaderboard.start_game("Mexico", "Canada")
        leaderboard.start_game("Spain", "Brazil")
        leaderboard.start_game("Germany", "France")
        leaderboard.start_game("Uruguay", "Italy")
        leaderboard.start_game("Argentina", "Australia")

        leaderboard.update_score("Mexico", "Canada", 0, 5)
        leaderboard.update_score("Spain", "Brazil", 10, 2)
        leaderboard.update_score("Germany", "France", 2, 2)
        leaderboard.update_score("Uruguay", "Italy", 6, 6)
        leaderboard.update_score("Argentina", "Australia", 3, 1)
        pass