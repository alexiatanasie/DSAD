import numpy as np
import graphics as g
import pandas as pd
import matplotlib.pyplot as plt


# create of matrix of (7, 10) of floating points values
# in [1, 10)
nda_1 = np.random.uniform(1, 10+1, (21, 12))
print(nda_1, type(nda_1))
corr = np.corrcoef(nda_1, rowvar=False)
# we assume to have the variables on the columns
print(corr)

# invoque the correlagram
# g.correlogram(corr, dec=1, title='Correlogram from numpy.ndarray')
# g.showImage()

# create a pandas.DataFrame from the numpy.ndarray
corr_df = pd.DataFrame(data=corr,
                     index=('V_'+str(i+1) for i in range(corr.shape[0])),
                     columns=('V_'+str(i+1) for i in range(corr.shape[0])))
# g.correlogram(corr_df, dec=1, title='Correlogram from pandas.DataFrame')
# g.showImage()

g.correlationCircle(corr, V1=2, V2=3, dec=1,
        title='Correlation Circle from numpy.ndarray')
g.correlationCircle(corr_df, V1=2, V2=3, dec=1,
        title='Correlation Circle from pandas.DataFrame')
# g.correlationCircle('my mom')

# the explained variance graph
# start with a randomly generated vector (eigenvector)
# of floating point values between [0, 8)
alpha = np.random.uniform(0, 3, size=15)
print(alpha, type(alpha))
alpha = np.sort(a=alpha)
alpha = alpha[::-1]
print(alpha, type(alpha))

g.explainedVariance(alpha)
g.showImage()

