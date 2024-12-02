import numpy as np


def replaceNAN(X):  # assume that we receive a numpy.ndarray
    means = np.nanmean(a=X, axis=0)  # we have the variables on the columns
    locs = np.where(np.isnan(X))
    print(locs, type(locs))
    X[locs] = means[locs[1]]
    return X
