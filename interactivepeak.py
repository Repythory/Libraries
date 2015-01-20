
def interactivepeak(data):
	"""
	data is a data set x,y
	Funny function: plot the data and for each clic point a maximum of the graph! 
	"""
		X,Y=data[:,0], data[:,1]
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(X,Y,label="prova") #plot the function
		#plt.legend(loc=1, ncol=1, shadow=True)
		plt.xlim(min(X) * 0.9, max(X) * 1.1)
		plt.ylim(min(Y) * 0.9, max(Y) * 1.1)
		plt.ylabel(r'Y axis')
		plt.xlabel(r'X axis')
		Diz=dict(zip(X,Y)) #create a dictionary that associate X with Y
		Interval=[] #interval where the user search for peaks
		PeaksList=[] #list of peaks found
		def onclick(event):
			print 'First limit at =%f'%(event.xdata)
			Interval.append(event.xdata)
			if len(Interval)%2==0:
				a=Interval[-2]       
				b=Interval[-1]    
				if b<a: #if the user select first the highest value these statements filp it!
					A=b
					B=a
				else:
					A=a
					B=b
			  #find the max Y value: the peak!
				peakY=0 #max Y value
				piccoX=0 #value of the X associate to the peak
				for i in [ j for j in X if A<j<B] :
					if Diz[i]>peakY:
						peakY=Diz[i]
						piccoX=i
				print "Interval: %f - %f  Peak at: %f " %(a,b,piccoX)
				PeaksList.append([piccoX,peakY])
				ax.annotate("picco", xy=(piccoX,peakY),  xycoords='data',
						xytext=(-50, 30), textcoords='offset points',
						arrowprops=dict(arrowstyle="->")
						)
				plt.draw()

		cid = fig.canvas.mpl_connect('button_press_event', onclick)
		
		return plt.show()     
