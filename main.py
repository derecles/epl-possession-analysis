"""
This script creates a csv file containing data on EPL teams' average percentage
possession per match and their average match outcome.
"""

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import os
import requests
import time
import urllib.request

# Setup [  ]

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

# Loop

"""
for season in match_id:
	for match in season:
		match_url = base_url + str(match)
		response = requests.get(match_url)
		soup = BeautifulSoup(response.text, 'html.parser')
		print(match_url)
"""

# Create a new file [OK]

"""
filename = 'epl_data.csv'

if os.path.exists(filename):
	os.remove(filename)

if not os.path.exists(filename):
	f = open(filename, 'a+')
"""

# Append the column labels [OK]

"""
label_str = 'name_home,pp_home,gs_home,pe_home,name_away,pp_away,gs_away,pe_away\n'
f.write(label_str)
"""

"""
# To do [  ]

# For each match, do the following:
	# 1) Get the 3-letter abbreviation for the home team	[OK]
	# 2) Get the % possession value for the home team
	# 3) Get the number of goals scored by the home team	[OK]
	# 4) Get the 3-letter abbrevation for the away team		[OK]
	# 5) Get the % possession value for the away team
	# 6) Get the number of goals scored by the away team	[OK]
	# 7) Get the number of points earned by the home team	[OK]
	# 8) Get the number of points earned by the away team	[OK]
	# 9) Append 1,2,3,7,4,5,6,8,newline						[  ]

# Iterate the above actions for each match for each season	[  ]
"""

"""
# 1) Get the 3-letter abbreviation for the home team	[OK]
name_home = soup.find('div', class_='teamScore').find_all('a')[0].contents[2][5:8];
"""

# 2) Get the % possession value for the home team		[  ]

# Use selenium webdriver to get data from dynamically generated HTML table
# Dynamically generated table contains % possession data
# https://stackoverflow.com/questions/17597424/how-to-retrieve-the-values-of-dynamic-html-content-using-python
# https://stackoverflow.com/questions/13960326/how-can-i-parse-a-website-using-selenium-and-beautifulsoup-in-python
# Get the dynamically allocated possession figures

driver = webdriver.Chrome()
driver.get('https://www.premierleague.com/match/38687')

# Testing

"""
match_url = base_url + str(38687)
response = requests.get(match_url)
"""

soup = BeautifulSoup(driver.page_source, 'html.parser')
# elem = soup.find_all('li', class_='active')
# elem = soup.findElement(By.XPATH('//li[@data-tab-index="2"]'))
elem = driver.find_element_by_css_selector('li[data-tab-index="2"]')
# elem.click()
print(elem)

"""
f.write(pp_home)
f.write(",")
"""

"""
# 3) Get the number of goals scored by the home team	[OK]
gs_home = soup.find('div', class_='score').contents[0]
"""

"""
# 4) Get the 3-letter abbrevation for the away team		[OK]
name_away = soup.find('div', class_='teamScore').find_all('a')[1].contents[0][5:8];
"""

# 5) Get the % possession value for the away team		[  ]


"""
# 6) Get the number of goals scored by the away team	[OK]
gs_away = soup.find('div', class_='score').contents[2]
"""

"""
# 7) Get the number of points earned by the home team	[OK]
pe_home = 0
if (gs_home > gs_away):
	pe_home = 3
elif (gs_home == gs_away):
	pe_home = 1
else:
	pe_home = 0

# 8) Get the number of points earned by the away team	[OK]
pe_away = 0
if (gs_away > gs_home):
	pe_away = 3
elif (gs_away == gs_home):
	pe_away = 1
else:
	pe_away = 0
"""


# 9) Append 1,2,3,7,4,5,6,8,newline						[ ]

"""
f.write(name_home)
f.write(",")

f.write(gs_home)
f.write(",")

f.write(str(pe_home))
f.write(",")

f.write(name_away)
f.write(",")

f.write(gs_away)
f.write(",")

f.write(str(pe_away))
f.write("\n")

f.close()
"""
