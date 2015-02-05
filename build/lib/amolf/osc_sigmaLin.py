	
def osc_sigmaLin(a,b,phi=0,T=24,A=10,llim=0,ulim=100,dx=0.1, r=15):
	"""
	Generate an oscillatory signal with withe gaussian noise around. The variance depend on x
	
	Compute the signal:
	
	y(x) = A sin(w t+ phi) +r +noise
		
		llim the starting point;
		ulim the ending; 
		dx the pass
		phi the phase 
		T the period,
		r around which value you want to oscillate
	
	w=2 Pi/T
	
	noise is gaussian BUT with the variance that depend on x:
	
	sigmax= b*x +a
	
	"""
	
	w=2 * pi/T

	d=arange(llim,ulim,dx)
	
	
	y=[]
	
	for i in d:
		y=list(y)
		j=A*sin(w*i + phi)+r
		
		#c=a*(1-exp(-j/b))
		
		c=b*j+a
		
		y.append(random.normal(0,c))
	
	
	y= A*sin(w*d + phi) + y	+r
	
	return d, y
