# fastreg

A faster regression routine for Python.

There are a number of regression routines for Python, but none of them handle
vectorised calculations (to my knowledge). A classic example of this problem is regression in
time of an array which includes spatial dimensions. A simple way to approach
this would be to loop over each spatial point. This approach is extremely slow.
A faster approach is to use matrix operations.

**fastreg** implements a vectorised ordinary least squares (OLS) linear
regression for used when the independent data vary only with time but the
dependent data vary in both time and space (a new version allowing the
independent data to also vary in space is planned).

The equation for the parameters of the OLS problem is:

![OLS equation](https://upload.wikimedia.org/math/b/8/d/b8dbcd12ae63080ec03d433eb4e4da8d.png)

**fastreg** implements this in Python and calculates the Pearson correlation coefficient, *p*-value for the hypothesis test whose null hypothesis is that the slope is zero, and the standard error for the slope estimate.
