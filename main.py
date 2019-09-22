"""
This script creates a csv file containing data on EPL teams' average percentage
possession per match and their average match outcome.
"""

from bs4 import BeautifulSoup

import os
import requests
import urllib.request

# Setup [OK]

base_url = 'https://www.premierleague.com/match/'

"""
match_id = [range(5567, 5947),
			range(5947, 6327),
			range(6327, 6707),
			range(6707, 7087),
			range(7087, 7467),
			range(7467, 7847),
			range(7864, 8244),
			range(9231, 9611),
			range(9611, 9991),
			range(12115, 12495),
			range(14040, 14420),
			range(22342, 22721),
			range(38308, 38688)]
"""

# Create a new file [OK]

"""
filename = 'epl_data.csv'

if os.path.exists(filename):
	os.remove(filename)

if not os.path.exists(filename):
	f = open(filename, 'a+')

# Write the column labels on the first row, separated by commas (except last column label)
label_str = 'name_home,%p_home,gs_home,pe_home,name_away,%p_away,gs_away,pe_away\n'
f.write(label_str)
f.close()
"""

# Scraping implementation [ ]

# For each match, do the following:
	# Get the 3-letter abbreviation for the home team, append to file
	# Append a comma
	# Get the 3-letter abbrevation for the away team, append to file
	# Append a comma
	# Get the % possession value for the home team, append to file
	# Append a comma
	# Get the % possession value for the away team, append to file
	# Append a comma
	# Get the number of goals scored by the home team, append to file
	# Append a comma
	# Get the number of goals scored by the away team, append to file
	# Append a comma
	# Get the number of points earned by the home team, append to file
	# Append a comma
	# Get the number of points earned by the away team, append to file
	# Append a newline

"""
match_url = base_url + str(i)
response = requests.get(match_url)
soup = BeautifulSoup(response.text, 'html.parser')
"""

# Get the 3-letter abbreviations for each team [ ]

"""
for x in soup.find_all('div', class_='timeLineContainer'):
	for y in x.find_all('a', class_='team'):
		temp = y.contents[2]
		print(temp)
"""

# Use selenium webdriver to get data from dynamically generated HTML table
# Dynamically generated table contains % possession data
# https://stackoverflow.com/questions/17597424/how-to-retrieve-the-values-of-dynamic-html-content-using-python
#  https://stackoverflow.com/questions/13960326/how-can-i-parse-a-website-using-selenium-and-beautifulsoup-in-python

"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('https://www.premierleague.com/match/38687')
# assert 'premierleague' in driver.title
elem = driver.find_element_by_name('tbody')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
assert 'No results found.' not in driver.page_source
driver.close()
"""

# Get the dynamically allocated possession figures

"""
x = soup.find('tbody', class_='matchCentreStatsContainer')
print(x)			
"""

# Get the goals scored by each team

"""
x = soup.find('div', class_='score')
unwanted = x.find('span')
unwanted.extract()
print(x.text)
"""

# Get points earned (pe) for both teams in a given match

def	calculate_points_earned(gsh, gsa):
	gs_home, gs_away = gsh, gsa
	pe_home, pe_away = 0, 0

	if (gs_home > gs_away):
		pe_home = 3
		pe_away = 0
	elif (gs_home < gs_away):
		pe_home = 0
		pe_away = 3
	else:
		pe_home, pe_away = 1

# Append everything to the file

# Testing

"""
match_url = base_url + str(38687)
response = requests.get(match_url)
soup = BeautifulSoup(response.text, 'html.parser')
"""
