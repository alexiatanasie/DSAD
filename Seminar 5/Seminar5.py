import pandas as pd
import numpy as np
import graphics as graph

#generate a matrix of(7,5) random integer values in [1,10]
nda1=np.random.randint(1,10+1,size=(7,5))
print(nda1,type(nda1))
print("\n")
#create a pandas.DataFrame from a numpy.ndarray
df1=pd.DataFrame(data=nda1)
print(df1,type(df1))
print("\n")

df2=pd.DataFrame(data=nda1,
                 index=('Line_'+str(i+1)for i in range(nda1.shape[0])),
                 columns=('Col_'+str(j+1)for j in range(nda1.shape[1])))
print(df2)
print("\n")

#accessing the labels for rows
print(df2.index,type(df2.index))
print(list(df2.index),type(list(df2.index)))
print("\n")

#accessing the labels for columns
print(df2.columns,type(df2.columns))
print(list(df2.columns),type(list(df2.columns)))
print("\n")

#accessing the values of a DataFrame
print(df2.values,type(df2.values))
print("\n")

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

#accessing cell in a pandas.DataFrame
print(df_4.iloc[0,1])
#iloc - utilizează numai pozițiile numerice ale rândurilor și coloanelor
print(df_4.loc['Line_1', 'Col_2'])
print(df_4['Col_1'])
print("\n")
# create a matrix of (10, 5) random floating point values
# in [1, 10]
nda_2 = np.random.uniform(1, 10+1, size=(20, 10)) #20 randuri, 10 coloane
print(nda_2)
print("\n")

#obtain the correlation matrix (PEARSON CORRELATION COEFFICIENT)
corr=np.corrcoef(nda_2,rowvar=False)
print(corr,"\n")

graph.Correlogram(corr, title="Correlogram from a numpy.ndarray")
corr_df = pd.DataFrame(data=corr,
                index=['V_'+str(i+1) for i in range(corr.shape[0])],
                columns=['V_'+str(i+1) for i in range(corr.shape[1])])
graph.Correlogram(corr_df, title='Correlogram from a pandas.DataFrame')

# generate a vector of 15 random values in [0, 3)
# and sort it in descending order
vect=np.random.uniform(0,3,size=15)
print(vect,type(vect))
vect=np.sort(a=vect)
vect=vect[::-1] #face ca secvența să fie parcursă de la final la început, inversând astfel ordinea elementelor
print(vect)

#ordine crescatoare
vector_1 = np.sort(vect)
print(vector_1)

#use the vector as eigenvalues sorted in descending order
graph.explainedVariance(vect)
graph.display()