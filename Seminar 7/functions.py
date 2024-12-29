import pandas as pd
import numpy as np

def dissimilarityIndex(df, colList):
    #fetch the ndarray from the dataframe
    X = df[colList].values
    print(X)
    #axes are counted from the right hand side
    #we do the sum on the lines
    sumsOnLines = np.sum(a=X, axis=1)
    print(sumsOnLines, len(sumsOnLines))
    #T is transposition of the matrix, np.transpose transposition method
    R = np.transpose(sumsOnLines-X.T)
    print(R, R.shape)
    #we do the sum on columns for each ethnicity
    Tx = np.sum(a=X, axis=0)
    print(Tx)
    Tr = np.sum(a=R, axis=0)
    print(Tr)
    print(Tx+Tr)
    #check if Tx and Tr contain zero and replace it with 1
    Tx[Tx==0] = 1
    Tr[Tr==0] = 1
    ratioX = X/Tx
    print(ratioX, ratioX.shape)
    ratioR = R/Tr
    result = 0.5*np.abs(ratioX-ratioR)
    print(result, result.shape)
    #we do the summing for each admin unit
    return np.sum(a=result, axis=1)


def entropyShannonWeaver(df, colList):
    #fetch the ndarray from the dataframe
    X = df[colList].values
    print(X)
    #axes are counted from the right hand side
    #we do the sum on the lines
    sumsOnLines = np.sum(a=X, axis=1)
    print(sumsOnLines, len(sumsOnLines))
    p = np.transpose(X.T / sumsOnLines)
    print(p, p.shape)
    # replace the zero values with 1 for the logarithmic function
    p[p == 0] = 1
    result = -1 * p * np.log2(p)
    print(result, result.shape)
    return np.sum(a=result, axis=1)  # compute the sums on the line,
    # for each administrative unit