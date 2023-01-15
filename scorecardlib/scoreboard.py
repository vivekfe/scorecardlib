from datetime import datetime
from scorecardlib.game import Game
from dataclasses import dataclass

@dataclass
class Scoreboard:
    games={}

    def start_game(self, home_team: str, away_team: str):
        """Calling this method with team names will add this as
        a key as joins of names and game  instance as value"""
        game = Game(home_team, away_team)
        self.games[f"{home_team}-{away_team}"] = game
