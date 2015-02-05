def _datacheck_peakdetect(x_axis, y_axis):
	"""
	You need to import this function in order to use peackdetect
	Basically it checks if the x_axis and y_axis are of the right type and lenght 
	
	Args:
		x_axis, y_axis: array of numbers where y(x)
	
	Returns: 
		x_axis, y_axis: if they are correct and in the right shape
	
	"""
	
	
	
    if x_axis is None:
        x_axis = range(len(y_axis))
    
    if len(y_axis) != len(x_axis):
        raise (ValueError, 
                'Input vectors y_axis and x_axis must have same length')
    
    #needs to be a numpy array
    y_axis = np.array(y_axis)
    x_axis = np.array(x_axis)
    return x_axis, y_axis
    
