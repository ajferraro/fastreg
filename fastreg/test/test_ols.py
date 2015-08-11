import numpy as np
from scipy import stats
import timeit

from fastreg import testdata, ols


def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped


def scipy_regression(xdata, ydata):
    if ydata.ndim > 1:
        nspat = ydata.shape[1]
    else:
        nspat = 1
    output = np.zeros((5,nspat))
    for i in xrange(nspat):
        output[:,i] = stats.linregress(xdata, ydata[:,i])
    return output


def test_ols_1d():
    xdata, ydata = testdata.generate_1d()
    reference = scipy_regression(xdata, ydata)
    output = ols.fit(xdata, ydata)
    assert np.isclose(reference, output).all()


def test_ols_2d():
    xdata, ydata = testdata.generate_2d()
    reference = scipy_regression(xdata, ydata)
    output = ols.fit(xdata, ydata)
    assert np.isclose(reference, output).all()
    wrapped_reference = wrapper(scipy_regression, xdata, ydata)
    time_reference = timeit.timeit(wrapped_reference, number=5)
    wrapped_output = wrapper(ols.fit, xdata, ydata)
    time_output = timeit.timeit(wrapped_output, number=5)
    assert time_output < time_reference
    speedup = time_reference / time_output
    print 'Fractional speedup: {:.0f}.0'.format(speedup)

