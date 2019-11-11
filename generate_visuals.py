from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

all_pp_pe = {}
last_season_pp_pe = {}

"""
# temp = teams.values()
# print(temp)

i = 0
for x in teams.values():
	# print(x.dtypes)
	print('XXXXXXXXXXXXXXXXXXXXX', i)
	i += 1
	print(x['match_date'])

	# if pd.to_datetime(x['match_date']) == '12/05/2019':
	# if x['match_date'].astype('datetime64') == '12/05/2019':
		# print(x)

	# temp = x['match_date'].astype('datetime64')
	# print(temp.dtypes)
"""

for team, dataset in teams.items():
	name_home = dataset[(dataset.name_home == team)]
	name_away = dataset[(dataset.name_away == team)]
	
	home_avg_pp = sum(name_home.pp_home) / len(name_home.pp_home)
	away_avg_pp = sum(name_away.pp_away) / len(name_away.pp_away)
	team_avg_pp = (home_avg_pp + away_avg_pp) / 2

	home_avg_pe = sum(name_home.pe_home) / len(name_home.pe_home)
	away_avg_pe = sum(name_away.pe_away) / len(name_away.pe_away)
	team_avg_pe = (home_avg_pe + away_avg_pe) / 2

	all_pp_pe[team_avg_pp] = team_avg_pe

x = np.array(list(all_pp_pe.keys())).reshape((-1, 1))
y = np.array(list(all_pp_pe.values()))
model = LinearRegression().fit(x,y)
y_pred = model.predict(x)
slope = model.coef_
intercept = model.intercept_
intercept = str(intercept)[1:7]
r_sq = model.score(x, y)

print('R-squared:', r_sq)
print('Regression equation: y = {:.4f}x - {}'.format(slope[0], intercept))

plt.scatter(x, y)
plt.plot(x, y_pred, color='red', label='y = {:.4f}x - {}'.format(slope[0], intercept))
plt.title('Possession vs. Match Outcomes')
plt.xlabel('Avg. Possession per Match (%)')
plt.xlim(left=40, right=60)
plt.xticks(np.arange(40, 61, 5))
plt.ylabel('Avg. Points Earned per Match')
plt.ylim(bottom=0.0, top=2.5)
plt.legend()
plt.show()
