def shannon_entropy(a,dx=1):
    """
    given:
        a: set of data
        dx: size of the bin that you imagine for this distribution, is a crucial ingredient for compute entropy
    
    return the shannon entropy of the distribution (http://en.wikipedia.org/wiki/Entropy_estimation)
    
    Important: the interval between the value of the sample a has to be the same ever! works with discrete set of data
    """

    h=[]
    bins=(a.max()-a.min())/dx
    bins=int(bins)
    if bins<=1: bins=2
    
    p,binedg= histogram(a,bins,normed=True)    
    bx=[x - binedg[i - 1] for i, x in enumerate(binedg)][1:]
    x=binedg[:-1]
    h=bx*p    
    g=-h*log2(p)
    g[isnan(g)]=0.    
    
    return g.sum()
    
    
def shannon_entropy2d(x,y, dx=1,dy=1):
    """
    Given 2 variables: x,y
    dx, dy : are the sizes of the bin that you imagine for this distribution, is a crucial ingredient for compute entropy
    
    return the shannon entropy of the whole system
    
    works properly if my arrays are arrays of int, with float is crucial set well the bin sizes
    
    """
    g=[]
    h=[]
    a= (x.max()-x.min())/dx
    b= (y.max()-y.min())/dy
    
    if a<=1: a=2
    if b<=1: b=2
    bins=[a,b]
    bins=array(bins)
    bins=bins.astype(int)
    c, xax, yax=histogram2d(x,y,100, normed=True)

    bx=[x - xax[i - 1] for i, x in enumerate(xax)][1:]
    by=[x - yax[i - 1] for i, x in enumerate(yax)][1:]
    h=[[x*bx[i]*by[j] for j, x in enumerate(row)] for i, row in enumerate(c)]

    xax=xax[:-1]
    yax=yax[:-1]
    p=h*log2(c)
    p[isnan(p)]=0.

    return -p.sum()
    
    
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
    hist,ax=histogramdd(c,bins,normed=True)
    
    binN=1.
    for i in range(0,len(ax)):
        if len(ax[i])>1: ax[i]=ax[i][:-1]
    for i in range(0,len(ax)):
        if len(ax[i])>1: binN=(float)(binN*(ax[i][1]-ax[i][0]))

    p1=hist*binN    
    p=-p1*log2(hist)
    p[isnan(p)]=0
    return p.sum()
	

def mutualinfo3d(t,x,y,dx):
	"""
	
	compute the mutual info that flow between x,y and t
	(they must have the same dimension!!!)
	***IMPORTANT is different if you want to copmute the mutual info between x;y;t
	*** IMPORTANT since the histograms are extrapolated from datas, means that in order to have a reasonable join ditribution the dimension of the array x,y,t have to be very large
		otherwise you do not have a good statistic and the mutual info copmuted is not precise (if the static is not enough it could be also totally non-sense!!!)
	
	Author: Michele Monti
	
	Args:
		[t,x,y]: input variables (arrays or lists) where you want to compute the mutual information that flows among (x,y) and t
	
	
		dx: list of bin sizes
	
	Returns:  
		info: Mutual information between x,y and t
	
	"""
	
	a = shannon_entropy(t, dx[0])
	b = shannon_entropydd([x, y], [dx[1], dx[2]])
	f = shannon_entropydd([t, x, y], dx)
	info = a + b - f
	return info
	

def mutualinfo2d(x,y,dx=0.05,dy=0.05):
	"""
	Right way to compute the mutual information between two variables x,y where
	y(x) 
	http://en.wikipedia.org/wiki/Information_theory
	
	Author: Michele Monti
	
	Args:
		x: set of data
		y: set of data (y(x) fit the definition!)
	Kwargs:
		[dx, dy] : are the sizes of the bin that you imagine for this distribution, is a crucial ingredient for compute entropy
	
	Returns:
	
		info: Mutual info between x ad y
	
	"""
	
	a = shannon_entropy(x, dx)
	b = shannon_entropy(y, dy)
	s = shannon_entropy2d(x, y, dx, dy)
	info = a + b - s
	return info