from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as seabornInstance

path = 'epl_data.csv'
dataset = pd.read_csv(path)

teams = {
	'ARS': dataset[(dataset.name_home == 'ARS') | (dataset.name_away == 'ARS')],
	'AVL': dataset[(dataset.name_home == 'AVL') | (dataset.name_away == 'AVL')],
	'BHA': dataset[(dataset.name_home == 'BHA') | (dataset.name_away == 'BHA')],
	'BIR': dataset[(dataset.name_home == 'BIR') | (dataset.name_away == 'BIR')],
	'BLB': dataset[(dataset.name_home == 'BLB') | (dataset.name_away == 'BLB')],
	'BLP': dataset[(dataset.name_home == 'BLP') | (dataset.name_away == 'BLP')],
	'BOL': dataset[(dataset.name_home == 'BOL') | (dataset.name_away == 'BOL')],
	'BOU': dataset[(dataset.name_home == 'BOU') | (dataset.name_away == 'BOU')],
	'BUR': dataset[(dataset.name_home == 'BUR') | (dataset.name_away == 'BUR')],
	'CAR': dataset[(dataset.name_home == 'CAR') | (dataset.name_away == 'CAR')],
	'CHA': dataset[(dataset.name_home == 'CHA') | (dataset.name_away == 'CHA')],
	'CHE': dataset[(dataset.name_home == 'CHE') | (dataset.name_away == 'CHE')],
	'CRY': dataset[(dataset.name_home == 'CRY') | (dataset.name_away == 'CRY')],
	'DER': dataset[(dataset.name_home == 'DER') | (dataset.name_away == 'DER')],
	'EVE': dataset[(dataset.name_home == 'EVE') | (dataset.name_away == 'EVE')],
	'FUL': dataset[(dataset.name_home == 'FUL') | (dataset.name_away == 'FUL')],
	'HUD': dataset[(dataset.name_home == 'HUD') | (dataset.name_away == 'HUD')],
	'HUL': dataset[(dataset.name_home == 'HUL') | (dataset.name_away == 'HUL')],
	'LEI': dataset[(dataset.name_home == 'LEI') | (dataset.name_away == 'LEI')],
	'LIV': dataset[(dataset.name_home == 'LIV') | (dataset.name_away == 'LIV')],
	'MCI': dataset[(dataset.name_home == 'MCI') | (dataset.name_away == 'MCI')],
	'MID': dataset[(dataset.name_home == 'MID') | (dataset.name_away == 'MID')],
	'MUN': dataset[(dataset.name_home == 'MUN') | (dataset.name_away == 'MUN')],
	'NEW': dataset[(dataset.name_home == 'NEW') | (dataset.name_away == 'NEW')],
	'NOR': dataset[(dataset.name_home == 'NOR') | (dataset.name_away == 'NOR')],
	'POR': dataset[(dataset.name_home == 'POR') | (dataset.name_away == 'POR')],
	'QPR': dataset[(dataset.name_home == 'QPR') | (dataset.name_away == 'QPR')],
	'RDG': dataset[(dataset.name_home == 'RDG') | (dataset.name_away == 'RDG')],
	'SHU': dataset[(dataset.name_home == 'SHU') | (dataset.name_away == 'SHU')],
	'SOU': dataset[(dataset.name_home == 'SOU') | (dataset.name_away == 'SOU')],
	'STK': dataset[(dataset.name_home == 'STK') | (dataset.name_away == 'STK')],
	'SUN': dataset[(dataset.name_home == 'SUN') | (dataset.name_away == 'SUN')],
	'SWA': dataset[(dataset.name_home == 'SWA') | (dataset.name_away == 'SWA')],
	'TOT': dataset[(dataset.name_home == 'TOT') | (dataset.name_away == 'TOT')],
	'WAT': dataset[(dataset.name_home == 'WAT') | (dataset.name_away == 'WAT')],
	'WBA': dataset[(dataset.name_home == 'WBA') | (dataset.name_away == 'WBA')],
	'WHU': dataset[(dataset.name_home == 'WHU') | (dataset.name_away == 'WHU')],
	'WIG': dataset[(dataset.name_home == 'WIG') | (dataset.name_away == 'WIG')],
	'WOL': dataset[(dataset.name_home == 'WOL') | (dataset.name_away == 'WOL')]
}

pp_pe = {}

for team, dataset in teams.items():
	name_home = dataset[(dataset.name_home == team)]
	name_away = dataset[(dataset.name_away == team)]
	
	home_avg_pp = sum(name_home.pp_home) / len(name_home.pp_home)
	away_avg_pp = sum(name_away.pp_away) / len(name_away.pp_away)
	avg_pp = (home_avg_pp + away_avg_pp) / 2

	home_avg_pe = sum(name_home.pe_home) / len(name_home.pe_home)
	away_avg_pe = sum(name_away.pe_away) / len(name_away.pe_away)
	avg_pe = (home_avg_pe + away_avg_pe) / 2

	pp_pe[avg_pp] = avg_pe

full = pd.DataFrame(list(pp_pe.items()), columns=['avg_pp', 'avg_pe'])

full.plot(x='avg_pp', y='avg_pe', style='o')
plt.title('Average possession versus match outcomes')
plt.xlabel('Average possession percentage per match (avg_pp)')
plt.ylabel('Average points earned per match (avg_pe)')
plt.show()
