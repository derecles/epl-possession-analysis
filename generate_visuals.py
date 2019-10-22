from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as seabornInstance

# %matplotlib inline

path = 'epl_data.csv'
names = ['name_home', 'pp_home', 'gs_home', 'pe_home', 'name_away', 'pp_away', 'gs_away', 'pe_away', 'match_date']
dataset = pd.read_csv(path)

"""
dim = dataset.shape
summaries = dataset.describe()
class_dist = dataset.groupby('name_home').size()
name_home_all = dataset.name_home.unique()
clubs = np.unique(dataset[['name_home', 'name_away']].values)
"""


ars = dataset[(dataset.name_home == 'ARS') | (dataset.name_away == 'ARS')]
avl = dataset[(dataset.name_home == 'AVL') | (dataset.name_away == 'AVL')]
bha = dataset[(dataset.name_home == 'BHA') | (dataset.name_away == 'BHA')]
bir = dataset[(dataset.name_home == 'BIR') | (dataset.name_away == 'BIR')]
blb = dataset[(dataset.name_home == 'BLB') | (dataset.name_away == 'BLB')]
blp = dataset[(dataset.name_home == 'BLP') | (dataset.name_away == 'BLP')]
bol = dataset[(dataset.name_home == 'BOL') | (dataset.name_away == 'BOL')]
bou = dataset[(dataset.name_home == 'BOU') | (dataset.name_away == 'BOU')]
bur = dataset[(dataset.name_home == 'BUR') | (dataset.name_away == 'BUR')]
car = dataset[(dataset.name_home == 'CAR') | (dataset.name_away == 'CAR')]
cha = dataset[(dataset.name_home == 'CHA') | (dataset.name_away == 'CHA')]
che = dataset[(dataset.name_home == 'CHE') | (dataset.name_away == 'CHE')]
cry = dataset[(dataset.name_home == 'CRY') | (dataset.name_away == 'CRY')]
der = dataset[(dataset.name_home == 'DER') | (dataset.name_away == 'DER')]
eve = dataset[(dataset.name_home == 'EVE') | (dataset.name_away == 'EVE')]
ful = dataset[(dataset.name_home == 'FUL') | (dataset.name_away == 'FUL')]
hud = dataset[(dataset.name_home == 'HUD') | (dataset.name_away == 'HUD')]
hul = dataset[(dataset.name_home == 'HUL') | (dataset.name_away == 'HUL')]
lei = dataset[(dataset.name_home == 'LEI') | (dataset.name_away == 'LEI')]
liv = dataset[(dataset.name_home == 'LIV') | (dataset.name_away == 'LIV')]
mci = dataset[(dataset.name_home == 'MCI') | (dataset.name_away == 'MCI')]
mid = dataset[(dataset.name_home == 'MID') | (dataset.name_away == 'MID')]
mun = dataset[(dataset.name_home == 'MUN') | (dataset.name_away == 'MUN')]
new = dataset[(dataset.name_home == 'NEW') | (dataset.name_away == 'NEW')]
nor = dataset[(dataset.name_home == 'NOR') | (dataset.name_away == 'NOR')]
por = dataset[(dataset.name_home == 'POR') | (dataset.name_away == 'POR')]
qpr = dataset[(dataset.name_home == 'QPR') | (dataset.name_away == 'QPR')]
rdg = dataset[(dataset.name_home == 'RDG') | (dataset.name_away == 'RDG')]
shu = dataset[(dataset.name_home == 'SHU') | (dataset.name_away == 'SHU')]
sou = dataset[(dataset.name_home == 'SOU') | (dataset.name_away == 'SOU')]
stk = dataset[(dataset.name_home == 'STK') | (dataset.name_away == 'STK')]
sun = dataset[(dataset.name_home == 'SUN') | (dataset.name_away == 'SUN')]
swa = dataset[(dataset.name_home == 'SWA') | (dataset.name_away == 'SWA')]
tot = dataset[(dataset.name_home == 'TOT') | (dataset.name_away == 'TOT')]
wat = dataset[(dataset.name_home == 'WAT') | (dataset.name_away == 'WAT')]
wba = dataset[(dataset.name_home == 'WBA') | (dataset.name_away == 'WBA')]
whu = dataset[(dataset.name_home == 'WHU') | (dataset.name_away == 'WHU')]
wig = dataset[(dataset.name_home == 'WIG') | (dataset.name_away == 'WIG')]
wol = dataset[(dataset.name_home == 'WOL') | (dataset.name_away == 'WOL')]
