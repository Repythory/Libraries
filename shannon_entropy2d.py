def shannon_entropy2d(x,y, dx=1,dy=1):
	"""
	Given 2 variables: x,y
	dx, dy : are the sizes of the bin that you imagine for this distribution, is a crucial ingredient for compute entropy
	
	
	return the shannon entropy of the whole system
	
	works properly if my arrays are arrays of int, with float is crucial set well the bin sizes
	
	"""
	a=(x.max()-x.min())/dx
	b= (y.max()-y.min())/dy
	
	if a<=1: a=2
	if b<=1: b=2
	h=[]
	bins=[a,b]
	
	bins=array(bins)
	
	bins=bins.astype(int)

	c, xax, yax=histogram2d(x,y,100, normed=True)

	bx=[x - xax[i - 1] for i, x in enumerate(xax)][1:]
	by=[x - yax[i - 1] for i, x in enumerate(yax)][1:]

	h=[[x*bx[i]*by[j] for j, x in enumerate(row)] for i, row in enumerate(c)]

	xax=xax[:-1]

	yax=yax[:-1]
	
	

	g=[]

	p=h*log2(c)
	p[isnan(p)]=0.


	return -p.sum()
