
def mutualinfo3d(t,x,y,dx):
	"""
	
	compute the mutual info that flow between x,y and t
	(they must have the same dimension!!!)
	***IMPORTANT is different if you want to copmute the mutual info between x;y;t
	*** IMPORTANT since the histograms are extrapolated from datas, means that in order to have a reasonable join ditribution the dimension of the array x,y,t have to be very large
		otherwise you do not have a good statistic and the mutual info copmuted is not precise (if the static is not enough it could be also totally non-sense!!!)
	
	Author: Michele Monti monti@amolf.nl
	
	Args:
		[t,x,y]: input variables (arrays or lists) where you want to compute the mutual information that flows among (x,y) and t
	
	
		dx: list of bin sizes
	
	Returns:  
		info: Mutual information between x,y and t
	
	"""
	
	c=[x,y]
	dxy=[dx[1],dx[2]]
	c1=[t,x,y]

	a=shannon_entropy(t,dx[0])
	b=shannon_entropydd(c,dxy)
	
	f=shannon_entropydd(c1,dx)
	
	info= a+b-f
	
	
	return info
