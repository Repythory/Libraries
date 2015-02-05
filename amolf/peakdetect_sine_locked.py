
def peakdetect_sine_locked(y_axis, x_axis, points = 9):
    """
    Convinience function for calling the 'peakdetect_sine' function with
    the lock_frequency argument as True.
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find peaks
    x_axis -- A x-axis whose values correspond to the y_axis list and is used
        in the return to specify the postion of the peaks.
    points -- (optional) How many points around the peak should be used during
        curve fitting, must be odd (default: 9)
        
    return -- see 'peakdetect_sine'
    """
    return peakdetect_sine(y_axis, x_axis, points, True)
    
    
