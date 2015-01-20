def mutualinfo2d(x,y,dx=0.05,dy=0.05):
	"""
	Right way to compute the mutual information between two variables x,y where
	y(x) 
	http://en.wikipedia.org/wiki/Information_theory
	
	x: set of data
	y set of data (y(x) fit the definition!)
	
	dx, dy : are the sizes of the bin that you imagine for this distribution, is a crucial ingredient for compute entropy
	
	
	
	"""
	
	#x1=tran(x,T,dx)
	
	a= shannon_entropy(x,dx)
	b=shannon_entropy(y,dy)
	s= shannon_entropy2d(x,y,dx,dy)
	
	return a+b -s
