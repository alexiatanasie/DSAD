import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# ex 3
#variance covariance matrix
raww=pd.read_csv('./dataIN/DataSet_83.csv',index_col=0)
labels=list(raww.columns.values)
rows=list(raww.index.values)

x=StandardScaler().fit_transform(raww)
cov=np.cov(x,rowvar=False)
pd.DataFrame(np.round(cov,2),index=labels,columns=labels).to_csv('./dataOUT/StdCov.csv')

"""interpretare: 
valoare pozitiva : corelatie directa: cand una creste ceallata tinde sa creasca
valoare negativa: corelatie inversa: cand una creste,cealalta tinde sa scada
"""

#ex 4 determine PCA
pca=PCA()
C=pca.fit_transform(x)
pd.DataFrame(np.round(C,2),index=rows,columns=['C'+str(i+1)for i in range(C.shape[1])]).to_csv('./dataOUT/Print.csv')
"""
C urile sunt componentele principale 
România are:
C1 = 0.58, C2 = 1.35
⇒ România este destul de influențată de componenta C2, într-o direcție pozitivă.

Belgia:
C1 = -1.86, C2 = -0.88
⇒ Belgia este în partea opusă față de România pe ambele componente.

"""

# ex 5 line plot
alpha=pca.explained_variance_

plt.figure(figsize=(7,7))
plt.title('variance explained by pca')
indexx=['C'+str(j+1)for j in range(len(alpha))]

plt.plot(indexx,alpha,'bo-')
plt.axhline(1,color='y')
plt.show()

"""
pe axa y am eigenvalues
linia orizontala la 1 este un prag important
criteriul kaiser pastrez componentele cu val > 1
acestea sunt considerate semnificative
"""

# ex 6 factor loading matrix and plot correlation circle
a=pca.components_.T

rxc=a*np.sqrt(alpha)

plt.figure(figsize=(7,7))
plt.title("factor loadings")

T=[t for t in np.arange(0,np.pi*2,0.01)]
X=[np.cos(t) for t in T]
Y=[np.sin(t) for t in T]
plt.plot(X,Y)
plt.axhline(0,c='r')
plt.axvline(0,c='y')
plt.scatter(rxc[:,0],rxc[:,1])
plt.show()

"""
Variabilele apropiate de cercul unitar au o contribuție semnificativă și sunt bine reprezentate în planul PC1–PC2.
 Poziția lor sugerează direcția și semnificația latentă a componentelor. 
 De exemplu, variabilele din cadranul dreapta sus contribuie pozitiv și semnificativ la ambele componente, în timp ce cele din stânga jos contribuie negativ.
 """
