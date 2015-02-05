
def shannon_entropydd(c,dx):
	"""
	Compute the shannon entropy of a set of n variable.
	
	c is a list of variables {x_i}(array) where you want to compute the entropy
	dx is the list of bin sizes

	return H({x_i}) = \int d{x_i} P({x_i} log2 P({x_i})


	"""
	bins2=[]
	
	bins=[]
	
	
	for i in range(0,len(c)):	
		nbin=(c[i].max()-c[i].min())/dx[i]
		if nbin>500: nbin =500
		
		bins2.append(nbin)
	
	bins2=array(bins2)
	
	bins=where(bins2==0,2,bins2)
	
	bins=array(bins)
	
	bins=bins.astype(int)
	
	#print bins
	#print 'shan dd'
	
	hist,ax=histogramdd(c,bins,normed=True)
	
	binN=1.
	for i in range(0,len(ax)):
		if len(ax[i])>1: ax[i]=ax[i][:-1]
	for i in range(0,len(ax)):
		if len(ax[i])>1: binN=(float)(binN*(ax[i][1]-ax[i][0]))
	
	#print binN
	
	p1=hist*binN
	
	p=-p1*log2(hist)
	
	p[isnan(p)]=0
	
	
	return p.sum()
