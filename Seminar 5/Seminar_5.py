import numpy as np
import pandas as pd
import graphics as graph


# generate a matrix of (7, 5) random integer values
# in [1, 10]
nda_1 = np.random.randint(1, 10+1, size=(7, 5))
print(nda_1, type(nda_1))

# create a pandas.DataFrame from a numpy.ndarray
df_1 = pd.DataFrame(data=nda_1)
print(df_1, type(df_1))
# provide explicit labels for columns and rows
df_2 = pd.DataFrame(data=nda_1,
    index=('Line_'+str(i+1) for i in range(nda_1.shape[0])),
    columns=('Col_'+str(j+1) for j in range(nda_1.shape[1])))
print(df_2)

# accessing the labels for rows
print(df_2.index, type(df_2.index))
print(list(df_2.index), type(list(df_2.index)))

# accessing labels for columns
print(df_2.columns, type(df_2.columns))

# accessing gthe values of a DataFrame
print(df_2.values, type(df_2.values))

# creating a pandas.DataFrame from a Python dictionary
# start for a dictionary with the keys in the format
# 'Col_1', 'Col_2', ..., 'Col_5'
# and as values a vector of 7 randomly generated integers in [1, 10]
dict_1 = {'Col_'+str(x+1):
          [y for y in np.random.randint(1, 10+1, 7)]
          for x in range(5)}
for (k, v) in dict_1.items():
    print(k, ":", v)

df_3 = pd.DataFrame(data=dict_1)
print(df_3)

# using s dictionary and provide labels for the rows
print(len(dict_1['Col_1']))

df_4 = pd.DataFrame(data=dict_1,
    index=('Line_'+str(i+1) for i in range(len(dict_1['Col_1']))))
print(df_4)

# accessing cells in a pandas.DataFrame
print(df_4.iloc[0, 1])
print(df_4.loc['Line_1', 'Col_2'])
print(df_4['Col_1'])

# create a matrix of (10, 5) random floating point values
# in [1, 10]
nda_2 = np.random.uniform(1, 10+1, size=(20, 10))
print(nda_2)
# obtain the correlation matrix (Pearson correlation coefficient)
corr = np.corrcoef(nda_2, rowvar=False)  # we have the variables on the columns
print(corr)

# graph.correlogram(corr, title="Correlogram from a numpy.ndarray")
corr_df = pd.DataFrame(data=corr,
                index=['V_'+str(i+1) for i in range(corr.shape[0])],
                columns=['V_'+str(i+1) for i in range(corr.shape[1])])
# graph.correlogram(corr_df, title='Correlogram from a pandas.DataFrame')

# graph.correlationCircle(corr, title='Correlation Circle from numpy.ndarray')
# graph.correlationCircle(corr_df, title='Correlation Circle from pandas.DataFrame')
# graph.correlationCircle('my mom')

# generate a vector of 15 random values in [0, 3)
# and sort it in descending order
vector_1 = np.random.uniform(0, 3, size=15)
print(vector_1, type(vector_1))
vector_1 = np.sort(a=vector_1)
vector_1 = vector_1[::-1]
print(vector_1)

# use the vector as eigenvalues sorted in descending order
graph.explainedVariance(vector_1)

graph.diplay()