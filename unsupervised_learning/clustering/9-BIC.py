#!/usr/bin/env python3
"""
Defines function that finds the best number of clusters for a GMM using
the Bayesian Information Criterion (BIC)
"""
import numpy as np

expectation_maximization = __import__('8-EM').expectation_maximization

def BIC(X, kmin=1, kmax=None, iterations=1000, tol=1e-5, verbose=False):
    """
    Finds the best number of clusters for a GMM using BIC
    """
    # Basic validation
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        return None, None, None, None
    if not isinstance(kmin, int) or kmin <= 0:
        return None, None, None, None
    if kmax is not None and (not isinstance(kmax, int) or kmax <= 0):
        return None, None, None, None
    if not isinstance(iterations, int) or iterations <= 0:
        return None, None, None, None
    if not isinstance(tol, (int, float)) or tol < 0:
        return None, None, None, None
    if not isinstance(verbose, bool):
        return None, None, None, None

    n, d = X.shape

    # If kmax is None, set it to maximum possible clusters
    if kmax is None:
        kmax = n

    if kmax < kmin:
        return None, None, None, None

    ks = list(range(kmin, kmax + 1))
    l = np.zeros(len(ks))
    b = np.zeros(len(ks))

    best_bic = None
    best_k = None
    best_result = None

    # At most ONE loop
    for i, k in enumerate(ks):
        try:
            pi, m, S, log_likelihood = expectation_maximization(
                X, k, iterations=iterations, tol=tol, verbose=verbose
            )
        except Exception:
            return None, None, None, None

        # Store log likelihood
        l[i] = log_likelihood

        # Number of parameters:
        # pi: k - 1 (since sum to 1)
        # means: k * d
        # covariances: k * d * (d + 1) / 2  (symmetric matrices)
        p = (k - 1) + k * d + k * (d * (d + 1) / 2)

        # BIC formula
        bic = p * np.log(n) - 2 * log_likelihood
        b[i] = bic

        # Track best (lowest BIC)
        if best_bic is None or bic < best_bic:
            best_bic = bic
            best_k = k
            best_result = (pi, m, S)

    return best_k, best_result, l, b
