

def neighbord_analysis(xas,col=0):
	"""
	Given an array xas this function compute the distance between the elements the mean distance and the variance
	
	Author: Michele Monti monti@amolf.nl
	
	Args:
			xas: the name of the list or data set that you want:
	

	Kwargs:
		col: is the column of the data set that you need to analyze


	Returns:
		c: the mean distance between neighbords, 
		d: stdeviation of the distances between neighbords.
		b: the difference between the first-neighbord in a list 
	"""
	xas=np.array(xas)
	
	
	a=xas
	if shape(xas)>1:
		a=xas[:,col]
	
	
	
	b=[x - a[i - 1] for i, x in enumerate(a)][1:]
	
	c=np.mean(b)
	d=np.std(b)
	
	return(b,c,d)
