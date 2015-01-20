
def intNd(c,axes):
    """ 
    c is a matrix n*n
    axes is a list of the corresponding coordinates
    
		return: the integral of c (n*n) array
	"""
    assert len(c.shape) == len(axes)
    assert all([c.shape[i] == axes[i].shape[0] for i in range(len(axes))])
    if len(axes) == 1:
        return scint.simps(c,axes[0])
    else:
        return intNd(scint.simps(c,axes[-1]),axes[:-1])

