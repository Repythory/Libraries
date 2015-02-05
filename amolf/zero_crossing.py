
def zero_crossings(y_axis, window = 11):
    """
    Algorithm to find zero crossings. Smoothens the curve and finds the
    zero-crossings by looking for a sign change.
    
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find zero-crossings
    window -- the dimension of the smoothing window; should be an odd integer
        (default: 11)
    
    return -- the index for each zero-crossing
    """
    # smooth the curve
    length = len(y_axis)
    x_axis = np.asarray(range(length), int)
    
    # discard tail of smoothed signal
    y_axis = _smooth(y_axis, window)[:length]
    zero_crossings = np.where(np.diff(np.sign(y_axis)))[0]
    indices = [x_axis[index] for index in zero_crossings]
    
    # check if zero-crossings are valid
    diff = np.diff(indices)
    if diff.std() / diff.mean() > 0.2:
        print diff.std() / diff.mean()
        print np.diff(indices)
        raise(ValueError, 
            "False zero-crossings found, indicates problem {0} or {1}".format(
            "with smoothing window", "problem with offset"))
    # check if any zero crossings were found
    if len(zero_crossings) < 1:
        raise(ValueError, "No zero crossings found")
    
    return indices 
