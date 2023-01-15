# Python Library for Foot Ball World Cup ScoreCard


![football-world-cup-2018](https://user-images.githubusercontent.com/435616/212528883-c69c0461-d632-49c9-af9b-97589bbf7251.jpg)



[Source-Wikimedia](https://www.publicdomainpictures.net/en/view-image.php?image=257160&picture=football-world-cup-2018)

# What is this Library

You are working in a sports data company, and we would like you to develop a new Live Football ##World Cup Scoreboard library (or frontend application) that shows all the ongoing matches and their ##scores.

### The scoreboard supports the following operations:

1. Start a new game, assuming initial score 0 – 0 and adding it the scoreboard.
This should capture following parameters:
  a. Home team
  b. Away team
2. Update score. This should receive a pair of absolute scores: home team score and away team score.

3. Finish game currently in progress. This removes a match from the scoreboard.

4. Get a summary of games in progress ordered by their total score. The games with the same total score will be returned ordered by the most recently started match in the scoreboard.

## This library contains two classes called Game and ScoreBoard. Below is how the classes look like - 

_Game class:_

**Properties:** home team, away team, home team score, away team score, start time, end time

**Methods:** update_score, finish_game, repr

_Scoreboard class_:

**Properties:** list of Match objects

**Methods:** start_game, update_score, finish_game, get_summary, repr

