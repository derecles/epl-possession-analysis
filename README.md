# epl-possession-analysis

In a given football match, is having more possession associated with an improved match outcome?

## Overview

I have analyzed all matches in the [English Premier League](https://www.premierleague.com/) from 2006/07 to 2018/19. (06/07 is the earliest season in which match-level possession figures are available.)

## Methodology

I have defined a match outcome as the points earned by a given team in a given match.

There are 3 potential outcomes to each match:
```
---------------------------------------------------------------------------------------------------
| Situation                                        | Outcome                                      |
---------------------------------------------------------------------------------------------------
| Team A scores more goals than Team B             | Team A earns 3 points; Team B earns 0 points |
---------------------------------------------------------------------------------------------------
| Team B scores more goals than Team A             | Team B earns 3 points; Team A earns 0 points |
---------------------------------------------------------------------------------------------------
| Team A and Team B score the same number of goals | Team A earns 1 point;  Team B earns 1 point  |
---------------------------------------------------------------------------------------------------
```

There are 20 teams in a given season.

The team that earns the most points after each of its 38 games played in a given season wins the league.

For each team, I have plotted the average possession per match across all matches in all season as the independent variable and the average points earned across all matches in all seasons as the dependent variable. A single data points represents a single team.

There are more than 20 data points because the English Premier League relegates the three teams with the fewest points earned after each season. The three relegated teams play in 2nd tier of English football in the season following their relegation from the Premier League.
