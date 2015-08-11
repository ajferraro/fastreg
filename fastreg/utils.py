"""Common utilities."""

import numpy as np


def add_constant(array):
    """Add an array of ones to allow for intercept calculation by ols.fit."""
    return np.c_[array, np.ones_like(array)]
