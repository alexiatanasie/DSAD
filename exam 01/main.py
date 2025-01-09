#sub 63 2024 V
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.preprocessing import StandardScaler


rawNatLoc=pd.read_csv('./dataIN/NatLocMovements.csv',index_col=0)
rawPop=pd.read_csv('./dataIN/PopulationLoc.csv',index_col=0)
labels=list(rawNatLoc.columns.values[1:]) #extract indicator labels

merged=rawNatLoc.merge(rawPop,right_index=True,left_index=True)[['City','CountyCode','Population']+labels]
merged.fillna(np.mean(merged[labels],axis=0),inplace=True)
'''
If any numeric data is missing in the labels columns, replace it with the mean:
python
index_col=0: Uses the first column in the CSV as the index.
Reset the Index If Needed:
df.reset_index(inplace=True)'''

#1
merged.groupby('CountyCode').sum()\
    .apply(lambda row:(row['LiveBirths']/(row['Population']/1000))-(row['Deceased']/(row['Population']/1000)),axis=1)\
    .to_csv('./dataOUT/Request_1.csv')
#axis =1 =>row by row
#axis=0 column by column

#2
#Calculate the cities with the highest indicator values per county ---
merged \
.set_index(['City', 'CountyCode']) \
.apply(lambda row: row[labels] / (row['Population'] / 1000), axis=1) \
.reset_index(1) \
.groupby('CountyCode') \
.apply(lambda df: pd.Series({lab: df[lab].idxmax() for lab in labels})) \
.to_csv('./dataOUT/Request_2.csv')


# reset_index(1): Scoate al doilea nivel de index (CountyCode) și îl transformă din nou într-o coloană.
'''{lab: df[lab].idxmax() for lab in labels}:

Pentru fiecare indicator (lab) din labels:
df[lab] este seria (coloana) indicatorului pentru grupul curent (CountyCode).
df[lab].idxmax() returnează indexul rândului (care este orașul) unde indicatorul are valoarea maximă.
Se creează un dicționar în care cheile sunt indicatorii din labels și valorile sunt orașele cu valorile maxime.
pd.Series(...): Transformă acest dicționar într-o serie Pandas.'''

#3 HCA ward
rawHealth=pd.read_csv('./dataIN/DataSet_34.csv',index_col=0)
#prima coloană din stânga fișierului CSV) nu va mai fi tratată ca parte a datelor obișnuite, ci va deveni indexul rândurilor din DataFrame.

x=StandardScaler().fit_transform(rawHealth)
pd.DataFrame(x,columns=rawHealth.columns.values).to_csv('./dataOUT/Xstd.csv')
HC=linkage(x,method='ward')
print(HC)
'''linkage din biblioteca scipy.cluster.hierarchy construiește un dendrogramă folosind o anumită metodă de legătură pentru a calcula distanțele dintre clustere.
Metoda Ward este o tehnică utilizată pentru a minimiza creșterea varianței intracluster la fiecare pas de aglomerare. Este cunoscută drept o metodă care creează clustere echilibrate și compacte.

Cum funcționează:
Începe cu fiecare punct de date ca fiind propriul său cluster.
La fiecare pas, combină perechea de clustere care duce la cea mai mică creștere a varianței totale intracluster.
Continuă până când toate punctele sunt într-un singur cluster.
Metoda Ward este adesea utilizată cu metrici de distanță bazate pe pătratul distanței euclidiene (în mod implicit).
'''
#4
# Calculate the threshold value with maximum difference
n=HC.shape[0] # nr total de pasi de aglomerare(nr de clustere combinate=nr de randuri din matricea HC
dist1=HC[1:n,2] #vectorul distantelor de aglomerare incepand de la al doilea rand
dist2=HC[0:n-1,2] #vect dist de aglom. pana la penultimul rand
diff=dist1-dist2
j=np.argmax(diff) #indicele unde diferenta dintre dist consecutive este cea mai mare
t=(HC[j,2]+HC[j+1,2])/2 #prag optim-nr optim de culstere

print('junction with max diff:',j)
print('threshold',np.round(t,2))

#5 dendrogram graphic for ex 4
plt.figure(figsize=(12,12))
plt.title('dendrogram')
dendrogram(HC,labels=rawHealth.index.values,leaf_rotation=45)
plt.axhline(t,c='r') #horizontal line
plt.show()
