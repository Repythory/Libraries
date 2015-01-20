def autocorrelation(x):
    """
    this function compute the autocorrelation of a signal x.
    http://en.wikipedia.org/wiki/Autocorrelation#Estimation
    http://stackoverflow.com/q/14297012/190597
    """
    n = len(x)
    variance = x.var()
    x = x-x.mean()
    r = np.correlate(x, x, mode = 'full')[-n:]
    assert np.allclose(r, np.array([(x[:n-k]*x[-(n-k):]).sum() for k in range(n)]))
    result = r/(variance*(np.arange(n, 0, -1)))
    return result
