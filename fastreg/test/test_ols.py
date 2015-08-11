"""Testing suite for fastreg.ols."""

import numpy as np
from scipy import stats
import timeit

from fastreg import testdata, ols


def wrapper(func, *args, **kwargs):
    """Wrapper to combine function and arguments for use with timeit."""
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def scipy_regression(xdata, ydata):
    """Standard, non-vectorised approach to regression using
    scipy.stats.linregress.  The spatial points are handled using a loop.

    Args:
        xdata (numpy.ndarray): 2D array of independent data [ntim, 1],
            where ntim is the number of time points (or other independent
            points). 
        ydata (numpy.ndarray): 2D array of dependent data [ntim, nspat],
            where nspat is the number of spatial points (or other dependent
            points).
     
    Returns:
        numpy.ndarray of dimension [5, nspat].  The 5 outputs are: slope, 
        intercept, Pearson's correlation coefficient, two-sided p-value for
        a hypothesis test with null hypothesis that the slope is zero, 
        standard error for the slope estimate.

    """
    # Calculate number of dimensions
    if ydata.ndim > 1:
        nspat = ydata.shape[1]
    else:
        nspat = 1

    # Calculate regression results, looping over the extra dimension
    output = np.zeros((5, nspat))
    for i in xrange(nspat):
        output[:, i] = stats.linregress(xdata, ydata[:, i])
    return output


def test_ols_1d():
    """Test the 1D case, where no looping is required."""
    xdata, ydata = testdata.generate_1d()
    reference = scipy_regression(xdata, ydata)
    output = ols.fit(xdata, ydata)
    assert np.isclose(reference, output).all()


def test_ols_2d():
    """Test the 2D case, where the scipy_regression function needs to loop
    and the ols.fit() function should deliver a significant speed-up.

    """
    # Check both give the same results
    xdata, ydata = testdata.generate_2d()
    reference = scipy_regression(xdata, ydata)
    output = ols.fit(xdata, ydata)
    assert np.isclose(reference, output).all()

    # Check speed-up
    wrapped_reference = wrapper(scipy_regression, xdata, ydata)
    time_reference = timeit.timeit(wrapped_reference, number=5)
    wrapped_output = wrapper(ols.fit, xdata, ydata)
    time_output = timeit.timeit(wrapped_output, number=5)
    assert time_output < time_reference
    speedup = time_reference / time_output
    print 'Fractional speedup: {:.0f}.0'.format(speedup)
