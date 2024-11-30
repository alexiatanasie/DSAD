import numpy as np
import pandas as pd
from  matplotlib.pyplot import title  #importa ftc title din modului matplotlib.p...
import graphics as graph

#generater a matrix of(7,5)random integer values in [1,10]
nda1=np.random.randint(1,10+1,size=(7,5))
print(type(nda1),nda1)

#create a pandas.DataFrame from a numpy.ndarray
df1=pd.DataFrame(data=nda1)
print(type(df1),df1)
#provide explicit labels for columns and rows
df2=pd.DataFrame(data=nda1,index=('Line'+str(i+1) for i in range(nda1.shape[0])),
                 columns=('Col '+str(j+1)for j in range(nda1.shape[1])))
print(df2)
#shape[0] nr de randuri din array(7)
#shape[1] nr de coloane din array(5)


#accessing labels for columns
print(df2.index,type(df2.index))
print(list(df2.index),type(list(df2.index)))

#accessing labels gor columns
print(df2.columns,type(df2.columns))

#accessing values of a DataFrame
print(df2.values,type(df2.values))

#create a pandas.DataFrame from a python dictionary
#start for a dictionary with the keys in the format: 'Col1','Col2',..'Col5'
#and as values a vector of 7 randomly generated integers in [1,10]

dict1 = {'Col'+str(x+1):
          [y for y in np.random.randint(1, 10+1, 7)]
          for x in range(5)}
for (k, v) in dict1.items():
    print(k, ":", v)

df3 = pd.DataFrame(data=dict1)
print(df3)

# using s dictionary and provide labels for the rows
print(len(dict1['Col1']))

df4 = pd.DataFrame(data=dict1,
    index=('Line'+str(i+1) for i in range(len(dict1['Col1']))))
print(df4)

#accessing cells in a pandas.DataFrame
print(df4.iloc[0,1])
print(df4.loc['Line1','Col2'])
print(df4['Col1'])


#create a matrix of (10,5) random floating point values in [1,10]
nda2=np.random.uniform(1,10+1,size=(20,10))
print(nda2)

#obtain the correlation matrix (Pearson correlation coefficient)
corr=np.corrcoef(nda2,rowvar=False) #we have the variables on the columns
print(corr)

graph.correlogram(corr,title="Correlogram from a numpy.ndarray")
corr=pd.DataFrame(data=corr,index=['V' +str(i+1) for i in range(corr.shape[0])],
                  columns=['V' +str(i+1)for i in range(corr.shape[1])])
graph.correlogram(corr,title='Correlogram from a pandas.DateFrame')
graph.display()