import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
import seaborn as sb
import matplotlib.pyplot as plt
from factor_analyzer import FactorAnalyzer, calculate_kmo

#load the dataset
dataset_file="DataSet_33.csv"
df=pd.read_csv(dataset_file)

#1 determine and save in the StdCov.csv file the variance-covariance matrix corresponding to the standardized numerical variables of the DataSet_33.csv

df_standardized = (df - df.mean()) / df.std()

#compute variance-covariance matrix
cov_matrix=np.cov(df_standardized.T) # T -transpusa
cov_df=pd.DataFrame(cov_matrix,index=df.columns,columns=df.columns)
stdcov_file="StdCov.csv"
cov_df.to_csv(stdcov_file)

# 2 PCA and save principal components
pca=PCA()
principal_components=pca.fit_transform(df_standardized)
pca_df=pd.DataFrame(principal_components,columns=['PC'+str(i+1)for i in range(principal_components.shape[1])])

# save  to PrinComp.csv
princomp_file="PrinComp.csv"
pca_df.to_csv(princomp_file,index=False)
# se pune index=false ca exclud index , adica first column (0,1,2..)

#3 plot explained variance
#marker='o': Adds circular markers for each principal component.
explained_variance=pca.explained_variance_ratio_
plt.figure(figsize=(10,6))
plt.plot(range(1,len(explained_variance)+1), explained_variance,marker='o',label='Explaind Variance')
plt.axhline(y=1/len(df.columns),color='r', linestyle='--',label='Variance=1/num_variables')
plt.title("explained variance by principal components")
plt.xlabel("principal component")
plt.ylabel("proportion of variance explained")
plt.legend()
plt.grid()
plt.show()

#4
#use Seaborn for heatmap
#import from factor_analyzer import FactorAnalyzer, calculate_kmo si SEABORN

#perform KMO test to check suitability for efa ???
kmo_value,kmo_model=calculate_kmo(df_standardized)
if kmo_model<0.6:
    print(kmo_model, "KMO measure is too low")
else:
    print(kmo_model,"KMO acceptable")


#perform factor analysis
n_factors=len(df.columns)-1 #set the nr of factors
fa=FactorAnalyzer(n_factors=n_factors,rotation="varimax")
#varimax is an orthogonal rotation method that maximizes the variance of squared loadings of a factor (column) across variables (rows).
fa.fit(df_standardized)

#extract factor loadings
factor_loadings=fa.loadings_

#create DataFrame for Factor Loadings
factor_loadings_df=pd.DataFrame(factor_loadings,index=df.columns,columns=['Factor'+str(i+1)for i in range(factor_loadings.shape[1])])

#round values to 2 decimal places for clarity
factor_loadings_df=factor_loadings_df.round(2)
def correlogram(x):
    """
    Plots a heatmap for the given matrix (factor loadings).
    :param x: The data matrix to plot (e.g., factor loading matrix).
    """
    plt.figure(figsize=(15, 11))
    plt.title("Correlogram of Factor Loadings")
    sb.heatmap(data=x, vmin=-1, vmax=1, cmap="bwr", annot=True)
    plt.show()

correlogram(factor_loadings_df)
print("Factor Loading Matrix:")
print(factor_loadings_df)


