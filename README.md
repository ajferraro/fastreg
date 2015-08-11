# fastreg

A faster regression routine for Python.

There are a number of regression routines for Python, but none of them handle
vectorised calculations. A classic example of this problem is regression in
time of an array which includes spatial dimensions. A simple way to approach
this would be to loop over each spatial point. This approach is extremely slow.
A faster approach is to use matrix operations.

**fastreg** implements a vectorised ordinary least squares (OLS) linear
regression for used when the independent data vary only with time but the
dependent data vary in both time and space (a new version allowing the
independent data to also vary in space is planned).

The equation for the parameters of the OLS problem is:

$\hat{\boldsymbol\beta} = (\mathbf{X}^{\rm T}\mathbf{X})^{-1} \mathbf{X}^{\rm T}\mathbf{y} = \big(\,{\textstyle\sum} \mathbf{x}_i \mathbf{x}^{\rm T}_i \,\big)^{-1} \big(\,{\textstyle\sum} \mathbf{x}_i y_i \,\big).$

**fastreg** implements this in Python and calculates the Pearson correlation coefficient, *p*-value for the hypothesis test whose null hypothesis is that the slope is zero, and the standard error for the slope estimate.
