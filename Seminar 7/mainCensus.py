from operator import index

import pandas as pd
import functions

dfLocalities = pd.read_csv(filepath_or_buffer='dataIN/Ethnicity.csv', index_col=0)
print(dfLocalities)

dfCounties = pd.read_excel('dataIN/CoduriRomania.xlsx', sheet_name='Localitati',
                           index_col=0)
print(dfCounties)

dfRegions = pd.read_excel('dataIN/CoduriRomania.xlsx', sheet_name=1,
                           index_col=0)
print(dfRegions)

dfMacroRegions = pd.read_excel('dataIN/CoduriRomania.xlsx', sheet_name=2,
                           index_col=0)
print(dfMacroRegions)

ethnicities = dfLocalities.columns.values[1:]
print(ethnicities, type(ethnicities))

#merge localities with counties
dfCountiesMerge = dfLocalities.merge(right=dfCounties, left_index=True,
                                     right_index=True)
print(dfCountiesMerge)
countyList = list(ethnicities)+['County']
print(countyList)
print(dfCountiesMerge[countyList])
#aggregate the localities for each county
dfCountyAgg = dfCountiesMerge[countyList].groupby(by='County').sum()
print(dfCountyAgg)
#save aggregation at the county level in a csv file
dfCountyAgg.to_csv('dataOUT/county ethnicity.csv')

#we need to merge the result of the county aggregation with the region codes
dfRegionsMerge = dfCountyAgg.merge(right=dfRegions, left_index=True,
                                    right_index=True)
print(dfRegionsMerge)

regionList = list(ethnicities)+['Regiune']
dfRegionAgg = dfRegionsMerge[regionList].groupby(by='Regiune').sum()
print(dfRegionAgg)
dfRegionAgg.to_csv('dataOUT/region ethnicity.csv')

dissim = functions.dissimilarityIndex(dfLocalities, ethnicities)
print(dissim, len(dissim))
dfDissimilarity = pd.DataFrame(data=dissim, columns=['Dissimilarity index'],
                               index=dfLocalities['City'].values)
print(dfDissimilarity)
dfDissimilarity.to_csv('dataOUT/dissimilarity index by localities.csv',
                index_label='Locality')

DI_county = functions.dissimilarityIndex(dfCountyAgg, ethnicities)
DI_county_df = pd.DataFrame(data=DI_county,
                        columns=['Dissimilarity index'],
                    index=dfRegions['NumeJudet'].values)
print(DI_county_df)
DI_county_df.to_csv('./dataOUT/DI_counties.csv',
                    index_label='County')

# call the function for computing the Shannon-Weaver entropy
SW_locality = functions.entropyShannonWeaver(dfLocalities, ethnicities)
SW_locality_df = pd.DataFrame(data=SW_locality,
                    columns=['Shannon-Weaver entropy'],
                    index=dfLocalities['City'].values)
print(SW_locality_df)
SW_locality_df.to_csv('./dataOUT/SW_entropy_localities.csv',
                    index_label='Locality')

# call th entropy at the county level
SW_county = functions.entropyShannonWeaver(dfCountyAgg, ethnicities)
SW_county_df = pd.DataFrame(data=SW_county,
                    columns=['Shannon-Weaver entropy'],
                    index=dfRegions['NumeJudet'].values)
print(SW_county_df)
SW_county_df.to_csv('./dataOUT/SW_entropy_counties.csv',
                index_label='County')
