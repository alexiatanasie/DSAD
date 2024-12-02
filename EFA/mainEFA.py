import numpy as np
import pandas as pd
import utils as utl
import efa.EFA as efa
import pca.PCA as pca
import factor_analyzer as fa
import visual as g
from sklearn.preprocessing import StandardScaler


tabel = pd.read_csv('dataIN/MortalityEU.csv',
                    index_col=0, na_values=':')
print(tabel)

obsNume = tabel.index.values
varNume = tabel.columns.values
matrice_numerica = tabel.values

# replace the missing values
X = utl.replaceNAN(matrice_numerica)
X_df = pd.DataFrame(data=X, index=obsNume, columns=varNume)
X_df.to_csv('./dataOUT/X.csv')

# compute Bartlett sphericity test
sphericityBartlett = fa.calculate_bartlett_sphericity(x=X_df)
print(sphericityBartlett)
if sphericityBartlett[0] > sphericityBartlett[1]:
    print('There is at least one common factor to be extracted!')
else:
    print('There are no common factors!')
    exit(-1)

# compute the Kaiser-Meyer-Olkin indices
kmo_idices= fa.calculate_kmo(x=X_df)
print(kmo_idices)
# check th emodel factorability based on the
# overall KMO index
if kmo_idices[1] > 0.5:
    print('The initial variables can be expressed through factors!')
else:
    print('There is no factor to expressed the causal variables!')
    exit(-2)

vector = kmo_idices[0]
print(vector, type(vector))
matrix = vector[:, np.newaxis]
print(matrix, type(matrix))
# obtain a pandas.DataFrame from the kmo matrix
kmo_df = pd.DataFrame(data=matrix, columns=['Kaiser-Meyer-Olkin Index'],
                    index=varNume)
print(kmo_df)

# call the intensity of link function
g.linkIntensity(matrice=kmo_df,
                titlu='Kaiser-Meyer-Olkin Indices')
g.afisare()