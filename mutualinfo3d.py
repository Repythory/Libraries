
def mutualinfo3d(t,x,y,dx):
	"""
	
	compute the mutual info that flow between x,y and t
	(they must have the same dimension!!!)
			note: is different if you want to copmute the mutual info between x;y;t
			
	t,x,y : input variables
	
	dx lis of bin sizes
	
	return : Mutual information between x,y and t
	
	"""
	
	c=[x,y]
	dxy=[dx[1],dx[2]]
	#t1=tran(t,T=24,dx=dx[0])
	c1=[t,x,y]

	a=shannon_entropy(t,dx[0])
	b=shannon_entropydd(c,dxy)
	
	f=shannon_entropydd(c1,dx)
	
	return a+b-f
