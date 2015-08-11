import numpy as np


def add_constant(array):
    return np.c_[array, np.ones_like(array)]
