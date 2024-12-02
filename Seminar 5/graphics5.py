import seaborn as sb
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#create a correlogram graphic
def Correlogram(R2,title='Correlogram',dec=2,minVal=-1,maxVal=1):
    plt.figure(num=title,figsize=(8,8))
    plt.title(title,fontsize=12,verticalalignment='bottom')
    sb.heatmap(data=np.round(R2,decimals=dec),vmin=minVal,vmax=maxVal,cmap='bwr',annot=True)

def correlationCircle(R2,k1=0,k2=1,dec=2,title='Correlation Circle'):
    plt.figure(num=title,figsize=(6,6))
    plt.title(title,fontsize=12,verticalalignment='bottom')
    theta=[t for t in np.range(0,np.pi*2,0.01)]

    x=[np.cos(t) for t in theta]
    y=[np.sin(t) for t in theta]
    plt.plot(x,y)
    plt.axhline(y=0,c='g')
    plt.axvline(x=0,c='g')

    if isinstance(R2,np.ndarray):
        plt.xlabel(xlabel='Variable' +str(k1+1), fontsize=10,color='Blue',
                 verticalalignment='top')
        plt.ylabel(ylabel='Variable' + str(k2 + 1), fontsize=10, color='Blue',
                   verticalalignment='top')
        plt.scatter(x=R2[:,k1],y=R2[:,k2],c='r')
        for i in range (R2.shape[0]):
            plt.text(x=R2[i,k1],y=R2[i,k2],\
                     s='('+str(np.round(R2[i,k2],decimals=dec))+')')

    elif isinstance(R2,pd.DataFrame):
        plt.xlabel(xlabel='Variable'+R2.columns.values[k1],fontsize=10,color='Blue',verticalalignment='top')
        plt.ylabel(ylabel='Variable'+R2.columns.values[k2],fontsize=10,color='Blue',verticalalignment='top')
        plt.scatter(x=R2.iloc[:,k1],y=R2.iloc[:,k2],c='k')
        for i in range (R2.index.values.shape[0]):
            plt.text(x=R2.iloc[i,k1],y=R2.iloc[i,k2],s=R2.index.values[i])

    else:
        raise Exception('input type is not supported')

    def explainedVariance(alpha,title='Explained variance by the principal components'):
        plt.figure(num=title,figsize=(10,6))
        plt.title(num=title,fontsize=12,verticalalignment='bottom')
        plt.xlabel(xlabel='Principal Components',fontsize=10,color='Blue',verticalalignment='bottom')
        Xvalues=['C'+str(i+1) for i in range (len(alpha))]
        plt.plot(Xvalues,alpha,'bo-',color='g')
        plt.axhline(y=1,c='r')

    def display():
        plt.show()

 #alpha:O listă sau un array care conține variațiile explicate de fiecare componentă principală.
 #Xvalues: Creează o listă de etichete pentru componentele principale
 # plt.plot :Creează un grafic de tip linie cu puncte
''''bo-':
b: Culoarea punctelor este albastră.
o: Punctele de pe grafic sunt marcate cu cercuri.
-: Punctele sunt conectate printr-o linie.

Culoarea liniei este setată explicit la verde (g).
'''