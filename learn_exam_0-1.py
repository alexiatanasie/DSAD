from socket import create_connection

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage,dendrogram,fcluster
from sklearn.preprocessing import StandardScaler

#ex 3  hca ward, standardised matrix
raww=pd.read_csv('./dataIN/DataSet_34.csv',index_col=0)

x=StandardScaler().fit_transform(raww)
pd.DataFrame(x,columns=raww.columns.values).to_csv('./dataOUT/Xstd.csv')

hc=linkage(x,method='ward') #aplica hierarchical clustering , met ward minimizeaza variatia interna totala
print(hc)

#cum intepretez rezultatul:
'''
tara cu indicele 9 este combinata cu tara cu indicele 19 , spatiul standardizat este 1.08, iar noul cluster contine 2 observatii(tari)

pe masura ce avansam clusterele cresc

ultimul rand e un cluster care contine toate cele 35 de tari la distanta maxima de 8.75
'''

#ex 4
#threshold and junction
n=hc.shape[0]
dist1=hc[1:n,2]
dist2=hc[0:n-1,2]
diff=dist1-dist2
j=np.argmax(diff) #gaseste indicele unde diferenta este maxima
t=(hc[j,2]+hc[j+1,2])/2 #calc threshold intre cele 2 distante care au facut saltul mai mare
#threshold este distanta la care putem taia dendograma pt a obtine cele mai coerente clustere

print("junction: ",j)
print("threshold",np.round(t,2))

#la pasul 32 din 34 diferenta este cea mai mare , in acel punct 2 clustere foarte diferite au fost unite
#distanta dintre acel pas si urmatorul este 8.16 - un prag natural pt taierea dendogramei

#5 dendogram graphic
plt.figure(figsize=(11,11))
plt.title('dendogram')
dendrogram(hc,labels=raww.index.values,leaf_rotation=45)
plt.axhline(t)
plt.show()

#culori sub linie ->5 clustere
"""Grupurile din partea de jos (cu distanță mică între ele) sunt cele mai omogene. 
Cu cât urcăm pe axa verticală, cu atât se unesc clustere tot mai diferite.
"""


#ex 6 OPTIMAL PARTITION
# tb sa dau import fluster la scipy.cl.hier
clusters=fcluster(hc,t,criterion='distance')
opt_part=pd.DataFrame(raww.index.values,clusters)
opt_part.to_csv('./dataOUT/Ystd.csv')