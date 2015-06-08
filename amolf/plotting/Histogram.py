def joinprob3d(ff, T1 = 2*pi):
	"""
	
	Given the 2d histogram (ff) of two datasets, this function gives back the join probability as 3d plot with the corresponding axis.
	
	Author: Michele Monti
	
	Args:
		ff: (list) is the output of histogram2d, 
			ff[0] is the distribution from histogram2d to 3d plot, ff[1] is the x axis, ff[2] the y axis
		
	Returns: the 3Dplot of the join distribution with the colorbar of the gradient!
	
	"""
	
	distribution = ff[0]
	fig = plt.figure()
	ax = fig.gca(projection = '3d')
	X, Y = meshgrid(ff[2][:-1], ff[1][:-1])	
		
	Gx, Gy = gradient(distribution)
	G = (Gx**2 + Gy**2) ** 0.5
	N = G/G.max()
	surf = ax.plot_surface(X, Y, distribution, rstride = 1, cstride = 1,
				facecolors = cm.jet(N),linewidth = 0, antialiased=False, shade=False)
	
	m = cm.ScalarMappable(cmap = cm.jet)
	m.set_array(G)
	plt.colorbar(m)
	
	return plt.show()
