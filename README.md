# epl-possession-analysis

In a given football (soccer) match, is having more possession of the ball associated with an improved match outcome?

## Overview

I have analyzed all of the matches played in the [Premier League](https://www.premierleague.com/) from 2006/07 to 2018/19.

2006/07 is the earliest season for which possession figures are available on the Premier League website.

## Methodology

I have defined a match outcome as the points earned by a given team in a given match.

There are 3 potential outcomes to a match based on the number of goals scored by each team:
```
---------------------------------------------------------------------------------------------------
| Goals Scored                                     | Outcome                                      |
---------------------------------------------------------------------------------------------------
| Team A scores more goals than Team B             | Team A earns 3 points; Team B earns 0 points |
---------------------------------------------------------------------------------------------------
| Team B scores more goals than Team A             | Team A earns 0 points; Team B earns 3 points |
---------------------------------------------------------------------------------------------------
| Team A and Team B score the same number of goals | Team A earns 1 point;  Team B earns 1 point  |
---------------------------------------------------------------------------------------------------
```

For each team, I have plotted the following:
- Independent variable: The given team's average possession percentage of the ball per match across all matches
- Dependent variable: The given team's average points earned per match across all matches

Each data point represents a single team.

I performed the analysis using three separate tools: Python, R, and Google Sheets. I was able to draw the same regression line (within a tight margin of error) using each tool independently.

## Scraping the data

**The script scrape.py is not going to stop until it has successfully completed, it is manually interrupted, or there is a network error during execution. As a result of explicit waits, this script will take at least 9.5 hours to complete and will repeatedly open and close Chrome instances. If the script is interrupted, the csv file will be deleted and re-created upon the next run.**

If you don't want to scrape the data, skip to the next section. The data is already contained in the following file:
```
epl_data.csv
```

If you _do_ want to scrape the data, you need to have [Selenium WebDriver](https://www.seleniumhq.org/) for Python installed. Once you are ready, run the following command in the cloned repo:
```
python3 scrape.py
```

This is going to create a csv file named epl_data.csv that contains the data to be analyzed. These will be the column labels:
```
--------------------------------------------------------------
| Column Label | Meaning                                     |
--------------------------------------------------------------
| name_home    | The name of the home team                   |
--------------------------------------------------------------
| pp_home      | The possession percentage for the home team |
--------------------------------------------------------------
| gs_home      | The goals scored by the home team           |
--------------------------------------------------------------
| pe_home      | The points earned by the home team          |
--------------------------------------------------------------
| name_away    | The name of the away team                   |
--------------------------------------------------------------
| pp_away      | The possession percentage for the away team |
--------------------------------------------------------------
| gs_away      | The goals scored by the away team           |
--------------------------------------------------------------
| pe_away      | The points earned by the away team          |
--------------------------------------------------------------
```

## Analyzing the data

In order to view a regression line drawn using Python, run this command:
```
python3 generate_visuals.py
```

In order to view a regression line drawn using R, use [RStudio](https://rstudio.com/) to run this R script:
```
generate_visuals.R
```

In order to view a regression line drawn using Google Sheets, open this pdf:
```
excel_visual.pdf
```

In order to view the Google Sheets input data, open this pdf:
```
excel_calculations.pdf
```

## Things to note

It is possible that at some point between the 2006/07 season and the 2018/19 season, the Premier League changed its methodology for calculating possession. If there was a change, the individual data points would be unlikely to change by a degree that is statistically significant. (If the calculation did change, I wasn't able to find an announcement.) However, you can approximate the possession percentage for Team A playing in a given match as follows:
```
Possession percentage for Team A = Passes completed by Team A / (Passes completed by Team A + Passes completed by Team B)
```

There are 20 teams that play in a given season. There are more than 20 data points because after each season, the Premier League relegates the 3 teams with the fewest points down to the [2nd tier](https://www.efl.com/) of the Premier League for the following season. The 3 teams from the 2nd tier that earned the most points in the 2nd tier are promoted up to the Premier League to replace the teams that were relegated.

If you want to play around with the raw data in a database, import this file to [sqlite3](https://www.sqlite.org/index.html) (recommended):
```
sqlite_epl_data.db
```

## To do

- [x] Analyze on a fully-aggregated basis (one plot, 39 data points)
- [ ] Analyze on a per-season basis (13 plots, 20 data points per plot)
- [ ] Analyze on a per-team basis (39 plots, variable number of data points per plot)
