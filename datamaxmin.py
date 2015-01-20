def datamaxmin(filename,xcol=0,ycol=1, graph='N'):
	"""
	filename is the name of the data file to analyze. It has to be .txt. 
	xcol is the column of the data file to se as the x axis 
	ycol is the column that hat to set as yaxis
	
	set graph='Y' if you want also the plot of the data and where max and min are.
	
	return:
		maxi list of the max (maxi[:,0] is the x-coordinate of the max, maxi[:,1] is the y)
		mini list of the min (mini[:,0] is the x-coordinate of the max, mini[:,1] is the y)
	
	"""
	data = np.loadtxt(filename)                       # myfile.txt is the file to import

	t,y=data[:,xcol], data[:,ycol]

	a=list(t)

	b=list(y)

	maxi,mini=peakdetect(b,x_axis=a)
	if graph=='Y':
		plt.plot(t,y)
		plt.plot(maxi[:,0],maxi[:,1],"o")
		plt.plot(mini[:,0],mini[:,1],"o")
		plt.show()
	
	return maxi,mini

	
