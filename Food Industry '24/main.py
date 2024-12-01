import pandas as pd
import numpy as np

'''In the IndustriaAlimentara.csv file there is information on the number of employees in the food industry at locality level. the informaton is as follows:
Siruta-Siruta code of the locality
City-name of the city
Meat,Fish,Vegetables, Fruits, Oils, Dairy, Milling, Bakery - the values representing the number of employees in the main activity in the food industry.

The PopulatieLocalitati.csv file constains the population by localities and thr county codes for each locality. in the files Coduri_Judete.csv and Coduri_Regiuni.csv there are codifications at the level of counties and regions.
'''

rawIndustrie=pd.read_csv('./dataIN/IndustriaAlimentara.csv',index_col=0)
rawCounties=pd.read_csv('./dataIN/Coduri_Judete.csv',index_col=0)
rawPop=pd.read_csv('./dataIN/PopulatieLocalitati.csv',index_col=0)
indLab=list(rawIndustrie.columns.values[1:])
#creează o listă care conține toate numele coloanelor din DataFrame-ul rawIndustrie, începând de la a doua coloană (ignorând prima).

merged = rawIndustrie[(rawIndustrie[rawIndustrie[indLab] > 0]).any(axis=1)] \
.merge(right=rawPop, left_index=True, right_index=True) \
.merge(right=rawCounties, left_on='Judet', right_index=True) \
.drop(['Localitate_y'], axis=1) \
.rename(columns={'Localitate_x': 'Localitate'})

#1
#save in the Requirement1.csv file the date on the nr of employees on food industry activities, for localities where the number of employees is greater than 0.
# The Requirement1.csv file will have the same columns as the IndustriaAlimentara.csv file.

filtered = merged[merged[indLab].sum(axis=1) > 0]

filtered[['Localitate'] + indLab] \
    .to_csv('./dataOUT/Requirement1.csv', index=False)

#2
# calculate and save in the Requirement2.csv file, the percentage of employees on each activity at locality level.


merged[['Localitate'] + indLab] \
.apply(lambda row: row[indLab] / row[indLab].sum() * 100, axis=1) \
.to_csv('./dataOUT/Requirement2.csv')

#3
# save in the Requirement3.csv file the counties sorted in descending order by the share of employees in the food industry in the total population.


merged[['NumeJudet', 'Populatie'] + indLab] \
.groupby('NumeJudet').sum() \
.apply(lambda row: row[indLab] / row['Populatie'], axis=1) \
.sum(axis=1) \
.sort_values(ascending=False) \
.to_csv('./dataOUT/Requirement3.csv')
#axis =1 - suma este calculata pe fiecare rand

#4
# save in the Requirement4.csv file, the activity with the most employees at the county level. The county code and the dominant activity will be displayed.

merged[['Judet'] + indLab] \
.groupby('Judet').sum() \
.idxmax(axis=1) \
.to_csv('./dataOUT/Requirement4.csv')

#5
# save in the Requirement5.csv file the average number of employees per activity at the region level. The weighted average will be calculated, using the population of the localities as weight.

merged[['Regiune', 'Populatie'] + indLab] \
.groupby('Regiune') \
.apply(lambda row: pd.Series({ind: np.average(row[ind], weights=row['Populatie']) for ind in indLab})) \
.to_csv('./dataOUT/Requirement5.csv')

# 6

# calculate and display in the file Requirement6.csv location indices at the county level for each activity.
# A location index is calculated as the ratio between the share of county i in activity j at the national level and the share of the population of county i in the total population.
#For example, if for county x the number of employees in the meat industry is 3000 people and the population is 200000 inhabitants, and at the national level the number of employees in the meat industry is 100000 people and the population of the country is 20000000 inhabitants, the index of location for the meat industry in county x is: (3000/100000)/(200000/20000000) = 3.

result = merged[['NumeJudet', 'Populatie'] + indLab] \
    .groupby('NumeJudet').sum()
result['Share'] = result[indLab].sum(axis=1) / result['Populatie']
result_sorted = result[['Share']].sort_values(by='Share', ascending=False)
result_sorted.to_csv('./dataOUT/Requirement3.csv')