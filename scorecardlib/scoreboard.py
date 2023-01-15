from datetime import datetime
from scorecardlib.game import Game
from dataclasses import dataclass, field
from typing import Dict
@dataclass
class Scoreboard:
    games: Dict[str, Game] = field(default_factory=dict)

    def start_game(self, home_team: str, away_team: str):
        """Calling this method with team names will add this as
        a key as joins of names and game  instance as value"""
        game = Game(home_team, away_team)
        self.games[f"{home_team}-{away_team}"] = game

    def check_if_match_ongoing(self, home_team, away_team):
        if not f"{home_team}-{away_team}" in self.games.keys():
            #validate if the given combination of teams exist in scoreboard
            raise Exception(f"There is no ongoing game between {home_team} and {away_team}\n")
        return True

    def update_score(self, home_team: str, away_team: str, home_score: int, away_score: int):
        """this method updates the score of any running games in scoreboard"""
        team_combination = f"{home_team}-{away_team}"
        if self.check_if_match_ongoing(home_team, away_team):
            self.games[team_combination].home_score= home_score
            self.games[team_combination].away_score= away_score

    def finish_game(self, home_team, away_team):
        pass
