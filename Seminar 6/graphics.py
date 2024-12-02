import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from openpyxl.styles.alignment import vertical_aligments


def correlogram(corr, dec=2, title='Correlogram',
                labelX='Variables on the X axis',
                labelY='Variables on the Y axis',
                valMin=-1,
                valMax=1):
    plt.figure(num=title, figsize=(12, 8))
    plt.title(label=title, fontsize=12)
    plt.xlabel(xlabel=labelX, fontsize=10)
    plt.ylabel(ylabel=labelY, fontsize=10)
    sb.heatmap(data=np.round(corr, decimals=dec),
               vmin=valMin,
               vmax=valMax, cmap='bwr',
               annot=True)

# see
# https://python-graph-gallery.com/92-control-color-in-seaborn-heatmaps/

def correlationCircle(R2, V1=0, V2=1, dec=2,
                      title='Correlation Circle',
        labelX='Variable 1', labelY='Variable 2'):
    # just to draw a circle
    plt.figure(num=title, figsize=(6, 6))
    plt.title(label=title, fontsize=12,
              verticalalignment='bottom')
    theta = [t for t in np.arange(0, np.pi * 2, 0.01, dtype=float)]
    print(theta)
    x = [np.cos(t) for t in theta]
    print(x)
    y = [np.sin(t) for t in theta]
    print(y)
    plt.plot(x, y)
    plt.axhline(y=0, c='g')
    plt.axvline(x=0, c='g')

    if isinstance(R2, np.ndarray):  # the correlation matrix is a numpy.ndarray
        plt.xlabel(xlabel='Variable ' + str(V1+1), fontsize=10)
        plt.ylabel(ylabel='Variable ' + str(V2+1), fontsize=10)
        plt.scatter(x=R2[:, V1], y=R2[:, V2], c='r')
        for i in range(R2.shape[0]):
            # plt.text(x=R2[i, V1], y=R2[i, V2], s='text')
            plt.text(x=R2[i, V1], y=R2[i, V2], s='(' +
            str(np.round(R2[i, V1], decimals=dec)) +
            ', ' + str(np.round(R2[i, V2], decimals=dec)) + ')')

    elif isinstance(R2, pd.DataFrame):
        plt.xlabel(xlabel=R2.columns[V1], fontsize=10)
        plt.ylabel(ylabel=R2.columns[V2], fontsize=10)
        plt.scatter(x=R2.iloc[:, V1], y=R2.iloc[:, V2], c='b')
        for i in range(len(R2.index)):  # R2.index.values.shape[0]
            plt.text(x=R2.iloc[i, V1], y=R2.iloc[i, V2],
            s=R2.index.values[i])

    else:
        raise Exception('Input type not supported!')


def explainedVariance(alpha, title='Explained Variance by '
                                   'the Principal Components'):
    plt.figure(num=title, figsize=(8, 6))
    plt.title(label=title, fontsize=12)
    plt.xlabel(xlabel='Principal Components', fontsize=10)
    plt.ylabel(ylabel='Eigenvalues - explained variance', fontsize=10)
    valuesX = ['C'+str(i+1) for i in range(len(alpha))]
    plt.plot(valuesX, alpha, 'bo-', c='b')
    plt.axhline(y=1, c='r')  # for Kayser criterion, have variance 1 emphasised

def showImage():
    plt.show()