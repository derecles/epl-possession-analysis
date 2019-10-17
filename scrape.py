"""
This script creates a csv file that contains data on EPL teams' average percentage
possession per match and their average match outcome.
"""

# [RESOLVED: Network connection issue]
# Error: Max retries exceeded with url: /match/6229
# NewConnectionError: Failed to establish a new connection
# Errno 8: nodename nor servname provided, or not known

# Error: NoneType for soup object at /match/6556

from bs4 import BeautifulSoup
from selenium import webdriver

import datetime
import os
import requests
import time
import urllib.request

def append_match_stats(match, f):
	print('Processing match: {}...'.format(str(match)[35:]))
	response = requests.get(match)
	soup = BeautifulSoup(response.text, 'html.parser')
	name_home = soup.find('div', class_='teamScore').find_all('a')[0].contents[2][5:8]
	name_away = soup.find('div', class_='teamScore').find_all('a')[1].contents[0][5:8]
	gs_home = soup.find('div', class_='score').contents[0]
	gs_away = soup.find('div', class_='score').contents[2]

	pe_home = 0
	if (gs_home > gs_away):
		pe_home = 3
	elif (gs_home == gs_away):
		pe_home = 1
	else:
		pe_home = 0

	pe_away = 0
	if (gs_away > gs_home):
		pe_away = 3
	elif (gs_away == gs_home):
		pe_away = 1
	else:
		pe_away = 0

	xpath_stats = "//li[contains(text(),'Stats')]"
	xpath_match_stats = "//li[contains(text(),'Match Stats')]"
	xpath_pp_home = "/html/body/main/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr[1]/td[1]/p"
	xpath_pp_away = "/html/body/main/div/section/div[2]/div[2]/div[2]/section[3]/div[2]/div[2]/table/tbody/tr[1]/td[3]/p"
	xpath_match_date = "/html/body/main/div/section/div[2]/section/div[1]/div/div[1]/div[1]"

	while True:
		try:
			driver = webdriver.Chrome()
			driver.get(match)
			time.sleep(3)
			click_stats = driver.find_element_by_xpath(xpath_stats).click()
			time.sleep(0.5)
			click_match_stats = driver.find_element_by_xpath(xpath_match_stats).click()
			time.sleep(2)
			global pp_home
			pp_home = driver.find_element_by_xpath(xpath_pp_home).text
			global pp_away
			pp_away = driver.find_element_by_xpath(xpath_pp_away).text
			global match_date
			match_date = driver.find_element_by_xpath(xpath_match_date).text
			match_date = datetime.datetime.strptime(match_date[4:], '%d %b %Y').strftime('%d/%m/%Y')
		except:
			continue
		finally:
			driver.quit()
			break

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
	f.write(',')
	f.write(str(match_date))
	f.write('\n')
	print('...done.')

if __name__ == '__main__':

	filename = 'epl_data.csv'

	"""

	# Don't touch this commented block unless you want to erase the csv and start from scratch!

	if os.path.exists(filename):
		os.remove(filename)
	if not os.path.exists(filename):
		f = open(filename, 'a+')
	label_str = 'name_home,pp_home,gs_home,pe_home,name_away,pp_away,gs_away,pe_away,match_date\n'
	f.write(label_str)

	"""

	if os.path.exists(filename):
		f = open(filename, 'a+')

	base_url = 'https://www.premierleague.com/match/'

	# EPL does not use any particular system for distributing match IDs
	# Each range represents all 380 matches in a given season, starting with 06/07 at index 0 until 18/19 at index 12
	match_id = [# range(5567, 5947),
				# range(5947, 6327),
				# range(6327, 6707),
				# range(6707, 7087),
				# range(7087, 7467),
				# range(7467, 7847),
				# range(7864, 8244),
				# range(9231, 9611),
				range(9292, 9611),
				range(9611, 9991),
				range(12115, 12495),
				range(14040, 14420),
				range(22342, 22721),
				range(38308, 38688)]

	# For each match, write match stats to csv
	for season in match_id:
		for match in season:
			append_match_stats(base_url + str(match), f)

	f.close()
