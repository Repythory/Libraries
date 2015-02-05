def shannon_entropy(a,dx=1):
	"""
	given:
		a: set of data
		dx: size of the bin that you imagine for this distribution, is a crucial ingredient for compute entropy
	
	return the shannon entropy of the distribution (http://en.wikipedia.org/wiki/Entropy_estimation)
	
	Important: the interval between the value of the sample a has to be the same ever! works with discrete set of data
	
	"""
	
	bins=(a.max()-a.min())/dx
	
	h=[]
	
	bins=int(bins)
	
	if bins<=1: bins=2
	
	#print bins
	#print 'shan 1d'
	
	p,binedg= histogram(a,bins,normed=True)
	
	bx=[x - binedg[i - 1] for i, x in enumerate(binedg)][1:]

	x=binedg[:-1]
	
	h=bx*p
	
	g=-h*log2(p)
	g[isnan(g)]=0.	
	return g.sum()
	
