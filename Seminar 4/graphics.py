import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np
#correlograma (reprezentare vizuala a unei matrice de corelatie), fol matplotlib si seaborn

#create a correlogram graphic
def correlogram(R2,title='Correlogram',
                 dec=2,minVal=-1, maxVal=1):
     #R2 can be either ndarray or DataFrame,
     #R2 reprez o matrice de corelatie.unde fiecare element indica relatia dintre 2 variabile
     #dex- precizia zecimalelor pt afisarea nr in matrice(2)
        plt.figure(num=title,figsize=(8,8)) #fig noua cu dim 8x8 inch
        plt.title(title,fontsize=12,verticalalignment='bottom') #seteaza titlul graficului
        sb.heatmap(data=np.round(R2,decimals=dec),vmin=minVal,vmax=maxVal,cmap='bwr',annot=True)
        #cmpa-colormap bwr-albastru pt val negative, rosu pt pozitive,alb pt zero
        #annot=True afiseaza val direct pe matrice in fiecare celula
def display():
    plt.show()