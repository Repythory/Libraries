
	
def joinprob3d(ff,T1=2*pi):
	"""
	
	Given the 2d Histogram (ff) of 2 set of data, this function give back the 3d plot of the join probability with the right axis.
	
	Author: Michele Monti monti@amolf.nl
	
	Args:
		ff: (list) is the output of histogram2d, 
			ff[0] is the distribution from histogram2d to 3d plot, ff[1] is the x axis, ff[2] the y axis
		
	Returns: the 3Dplot of the join distribution with the colorbar of the gradient!
	
	"""
	
	
	
	c=ff[0]
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	Y = ff[1][:-1]
	X = ff[2][:-1]
	X, Y = meshgrid(X, Y)	
		
	Gx, Gy = gradient(c) # gradients with respect to x and y
	G = (Gx**2+Gy**2)**.5  # gradient magnitude
	N = G/G.max()
		
	surf = ax.plot_surface(X, Y, c, rstride=1, cstride=1,facecolors=cm.jet(N),linewidth=0, antialiased=False, shade=False)
	
	m = cm.ScalarMappable(cmap=cm.jet)
	m.set_array(G)
	plt.colorbar(m)
	return plt.show()
