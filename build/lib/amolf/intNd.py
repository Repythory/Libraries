
def intNd(c,axes):
    """ 
    
    Having a n*n matrix that correspond to the value of a function with n arguments (n axes)
    this function give back the integral of this function using the axes that you select
    
    Author: Michele Monti monti@amolf.nl	
    
    Args:
		c: is a matrix n*n
		axes: is a list of the corresponding coordinates
    
	Returns: the integral of c (n*n) using axes
	
	
	"""
    assert len(c.shape) == len(axes)
    assert all([c.shape[i] == axes[i].shape[0] for i in range(len(axes))])
    if len(axes) == 1:
        return scint.simps(c,axes[0])
    else:
        return intNd(scint.simps(c,axes[-1]),axes[:-1])

