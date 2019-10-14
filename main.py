"""
This script creates a csv file containing data on EPL teams' average percentage
possession per match and their average match outcome.
"""

from bs4 import BeautifulSoup
from selenium import webdriver

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

# Loop [  ]

"""
for season in match_id:
	for match in season:
		match_url = base_url + str(match)
		response = requests.get(match_url)
		soup = BeautifulSoup(response.text, 'html.parser')
		print(match_url)
"""

# Create a new file [OK]

filename = 'epl_data.csv'

if os.path.exists(filename):
	os.remove(filename)

if not os.path.exists(filename):
	f = open(filename, 'a+')

# Append the column labels [OK]

label_str = 'name_home,pp_home,gs_home,pe_home,name_away,pp_away,gs_away,pe_away\n'
f.write(label_str)

# Test single single match (38687)

match_url = base_url + str(38687)
response = requests.get(match_url)
soup = BeautifulSoup(response.text, 'html.parser')

# Get the 3-letter abbreviation for the home team [OK]

name_home = soup.find('div', class_='teamScore').find_all('a')[0].contents[2][5:8]

# Get the 3-letter abbrevation for the away team [OK]

name_away = soup.find('div', class_='teamScore').find_all('a')[1].contents[0][5:8]

# Get the number of goals scored by the home team [OK]

gs_home = soup.find('div', class_='score').contents[0]

# Get the number of goals scored by the away team [OK]

gs_away = soup.find('div', class_='score').contents[2]

# Get the number of points earned by the home team [OK]

pe_home = 0
if (gs_home > gs_away):
	pe_home = 3
elif (gs_home == gs_away):
	pe_home = 1
else:
	pe_home = 0

# Get the number of points earned by the away team [OK]

pe_away = 0
if (gs_away > gs_home):
	pe_away = 3
elif (gs_away == gs_home):
	pe_away = 1
else:
	pe_away = 0

# Initialize new browser instance [OK]

driver = webdriver.Chrome()
driver.get('https://www.premierleague.com/match/38687')

# Simulate two click events in order to generate dynamic HTML [OK]

click_stats = driver.find_element_by_xpath("//li[contains(text(),'Stats')]").click()
click_match_stats = driver.find_element_by_xpath("//li[contains(text(),'Match Stats')]").click()
time.sleep(2)

# Get the % possession value for the home team [OK]

pp_home = driver.find_element_by_xpath("/html/body/main/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr[1]/td[1]/p").text

# Get the % possession value for the away team [OK]

pp_away = driver.find_element_by_xpath("/html/body/main/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr[1]/td[3]/p").text

# Terminate new browser instance [OK]

driver.quit()

# Append 1,2,3,7,4,5,6,8,newline [OK]

f.write(name_home)
f.write(',')
f.write(pp_home)
f.write(',')
f.write(gs_home)
f.write(',')
f.write(str(pe_home))
f.write(',')
f.write(name_away)
f.write(',')
f.write(pp_away)
f.write(',')
f.write(gs_away)
f.write(',')
f.write(str(pe_away))
f.write('\n')

f.close()
