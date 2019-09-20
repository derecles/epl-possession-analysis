"""
This script creates a csv file containing data on EPL teams' average percentage
possession per match and their average match outcome.
"""

from bs4 import BeautifulSoup

import os
import requests
import urllib.request

# Create a new file

filename = 'epl_data.csv'

"""
if os.path.exists(filename):
	os.remove(filename)
else:
	file_obj = open(filename, 'w+')
"""

# Get the data

big_str = 'name_home,%p_home,gs_home,pe_home,name_away,%p_away,gs_away,pe_away\n'


base_url = 'https://www.premierleague.com/match/'
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
for i in match_id[0]:
	match_url = base_url + str(i)
	response = requests.get(match_url)
	soup = BeautifulSoup(response.text, 'html.parser')
"""

match_url = base_url + str(38687)
response = requests.get(match_url)
soup = BeautifulSoup(response.text, 'html.parser')
for x in soup.find_all('div', class_='timeLineContainer'):
	temp = x.find('a', class_='team').contents[2]
	print(temp)

# Get points earned (pe) for both teams in a given match

gs_home = 0
pe_home = 0

gs_away = 0
pe_away = 0


