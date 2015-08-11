import numpy as np


def generate_2d():
    N = 50
    M = 1000
    x = np.random.rand(N)
    beta = np.random.rand(M, 1)
    Y = beta*x
    Y += np.random.normal(scale=0.1, size=Y.shape)
    return x, Y.T


def generate_1d():
    ndata = 100
    xdata = np.arange(ndata)
    ydata = 2*xdata + np.random.normal(scale=0.1, size=ndata)
    return xdata, ydata[:, np.newaxis]
