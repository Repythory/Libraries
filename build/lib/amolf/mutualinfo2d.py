def mutualinfo2d(x,y,dx=0.05,dy=0.05):
	"""
	Right way to compute the mutual information between two variables x,y where
	y(x) 
	http://en.wikipedia.org/wiki/Information_theory
	
	Author: Michele MOnti monti@amolf.nl
	
	Args:
		x: set of data
		y: set of data (y(x) fit the definition!)
	Kwargs:
		[dx, dy] : are the sizes of the bin that you imagine for this distribution, is a crucial ingredient for compute entropy
	
	Returns:
	
		info: Mutual info between x ad y
	
	"""
	
	
	
	a= shannon_entropy(x,dx)
	b=shannon_entropy(y,dy)
	s= shannon_entropy2d(x,y,dx,dy)
	info =a+b-s
	
	return info
