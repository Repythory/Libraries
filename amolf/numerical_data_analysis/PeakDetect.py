def peakdetect_list(y_axis, x_axis = None, lookahead = 45, delta=0):
    """
    Converted from/based on a MATLAB script at: 
    http://billauer.co.il/peakdet.html
    
    function for detecting local maximas and minmias in a signal.
    Discovers peaks by searching for values which are surrounded by lower
    or larger values for maximas and minimas respectively
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find peaks
    x_axis -- (optional) A x-axis whose values correspond to the y_axis list
        and is used in the return to specify the postion of the peaks. If
        omitted an index of the y_axis is used. (default: None)
    lookahead -- (optional) distance to look ahead from a peak candidate to
        determine if it is the actual peak (default: 200) 
        '(sample / period) / f' where '4 >= f >= 1.25' might be a good value
    delta -- (optional) this specifies a minimum difference between a peak and
        the following points, before a peak may be considered a peak. Useful
        to hinder the function from picking up false peaks towards to end of
        the signal. To work well delta should be set to delta >= RMSnoise * 5.
        (default: 0)
            delta function causes a 20% decrease in speed, when omitted
            Correctly used it can double the speed of the function
    
    return -- two lists [max_peaks, min_peaks] containing the positive and
        negative peaks respectively. Each cell of the lists contains a tupple
        of: (position, peak_value) 
        to get the average peak value do: np.mean(max_peaks, 0)[1] on the
        results to unpack one of the lists into x, y coordinates do: 
        x, y = zip(*tab)
        
        remember that if you want use like array this function give back to you 2 list, so you have to converter!!)
        
    """
    max_peaks = []
    min_peaks = []
    dump = []
    
    x_axis, y_axis = _datacheck_peakdetect(x_axis, y_axis)
    length = len(y_axis)
    if lookahead < 1:
        raise ValueError, "Lookahead must be '1' or above in value"
    if not (np.isscalar(delta) and delta >= 0):
        raise ValueError, "delta must be a positive number"
    
    mn, mx = np.Inf, -np.Inf
    for index, (x, y) in enumerate(zip(x_axis[:-lookahead], y_axis[:-lookahead])):
        if y > mx:
            mx = y
            mxpos = x
        if y < mn:
            mn = y
            mnpos = x
    
        if y < mx-delta and mx != np.Inf:
            if y_axis[index:index+lookahead].max() < mx:
                max_peaks.append([mxpos, mx])
                dump.append(True)
                mx = np.Inf
                mn = np.Inf
                if index+lookahead >= length:
                    break
                continue
    
        if y > mn+delta and mn != -np.Inf:
            if y_axis[index:index+lookahead].min() > mn:
                min_peaks.append([mnpos, mn])
                dump.append(False)
                mn = -np.Inf
                mx = -np.Inf
                if index+lookahead >= length:
                    break
    
    try:
        if dump[0]:
            max_peaks.pop(0)
        else:
            min_peaks.pop(0)
        del dump
    except IndexError:
        pass
        
    return [max_peaks, min_peaks]
    
    
def peakdetect_fft(y_axis, x_axis, pad_len = 5):
    """
    Performs a FFT calculation on the data and zero-pads the results to
    increase the time domain resolution after performing the inverse fft and
    send the data to the 'peakdetect' function for peak 
    detection.
    
    Omitting the x_axis is forbidden as it would make the resulting x_axis
    value silly if it was returned as the index 50.234 or similar.
    
    Will find at least 1 less peak then the 'peakdetect_zero_crossing'
    function, but should result in a more precise value of the peak as
    resolution has been increased. Some peaks are lost in an attempt to
    minimize spectral leakage by calculating the fft between two zero
    crossings for n amount of signal periods.
    
    The biggest time eater in this function is the ifft and thereafter it's
    the 'peakdetect' function which takes only half the time of the ifft.
    Speed improvementd could include to check if 2**n points could be used for
    fft and ifft or change the 'peakdetect' to the 'peakdetect_zero_crossing',
    which is maybe 10 times faster than 'peakdetct'. The pro of 'peakdetect'
    is that it resutls in one less lost peak. It should also be noted that the
    time used by the ifft function can change greatly depending on the input.
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find peaks
    x_axis -- A x-axis whose values correspond to the y_axis list and is used
        in the return to specify the postion of the peaks.
    pad_len -- (optional) By how many times the time resolution should be
        increased by, e.g. 1 doubles the resolution. The amount is rounded up
        to the nearest 2 ** n amount (default: 5)
    
    return -- two lists [max_peaks, min_peaks] containing the positive and
        negative peaks respectively. Each cell of the lists contains a tupple
        of: (position, peak_value) 
        to get the average peak value do: np.mean(max_peaks, 0)[1] on the
        results to unpack one of the lists into x, y coordinates do: 
        x, y = zip(*tab)
    """
    x_axis, y_axis = _datacheck_peakdetect(x_axis, y_axis)
    zero_indices = zero_crossings(y_axis, window = 11)
    last_indice = - 1 - (1 - len(zero_indices) & 1)
    fft_data = fft(y_axis[zero_indices[0]:zero_indices[last_indice]])
    padd = lambda x, c: x[:len(x) // 2] + [0] * c + x[len(x) // 2:]
    n = lambda x: int(log(x)/log(2)) + 1
    fft_padded = padd(list(fft_data), 2 ** n(len(fft_data) * pad_len) - len(fft_data))
    
    sf = len(fft_padded) / float(len(fft_data))
    y_axis_ifft = ifft(fft_padded).real * sf #(pad_len + 1)
    x_axis_ifft = np.linspace(
                x_axis[zero_indices[0]], x_axis[zero_indices[last_indice]],
                len(y_axis_ifft))

    max_peaks, min_peaks = peakdetect(y_axis_ifft, x_axis_ifft, 500, delta = abs(np.diff(y_axis).max() * 2))
    data_len = int(np.diff(zero_indices).mean()) / 10
    data_len += 1 - data_len & 1
    
    fitted_wave = []
    for peaks in [max_peaks, min_peaks]:
        peak_fit_tmp = []
        index = 0
        for peak in peaks:
            index = np.where(x_axis_ifft[index:]==peak[0])[0][0] + index
            x_fit_lim = x_axis_ifft[index - data_len // 2:
                                    index + data_len // 2 + 1]
            y_fit_lim = y_axis_ifft[index - data_len // 2:
                                    index + data_len // 2 + 1]
            
            peak_fit_tmp.append([x_fit_lim, y_fit_lim])
        fitted_wave.append(peak_fit_tmp)
    
    return [max_peaks, min_peaks]
    
    
    def peakdetect_parabole(y_axis, x_axis, points = 9):
    """
    Function for detecting local maximas and minmias in a signal.
    Discovers peaks by fitting the model function: y = k (x - tau) ** 2 + m
    to the peaks. The amount of points used in the fitting is set by the
    points argument.
    
    Omitting the x_axis is forbidden as it would make the resulting x_axis
    value silly if it was returned as index 50.234 or similar.
    
    will find the same amount of peaks as the 'peakdetect_zero_crossing'
    function, but might result in a more precise value of the peak.
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find peaks
    x_axis -- A x-axis whose values correspond to the y_axis list and is used
        in the return to specify the postion of the peaks.
    points -- (optional) How many points around the peak should be used during
        curve fitting, must be odd (default: 9)
    
    return -- two lists [max_peaks, min_peaks] containing the positive and
        negative peaks respectively. Each cell of the lists contains a list
        of: (position, peak_value) 
        to get the average peak value do: np.mean(max_peaks, 0)[1] on the
        results to unpack one of the lists into x, y coordinates do: 
        x, y = zip(*max_peaks)
    """
    max_peaks = []
    min_peaks = []
    x_axis, y_axis = _datacheck_peakdetect(x_axis, y_axis)
    points += 1 - (points % 2)
    
    max_raw, min_raw = peakdetect_zero_crossing(y_axis)
    max_ = _peakdetect_parabole_fitter(max_raw, x_axis, y_axis, points)
    min_ = _peakdetect_parabole_fitter(min_raw, x_axis, y_axis, points)
    
    max_peaks = map(lambda x: [x[0], x[1]], max_)
    max_fitted = map(lambda x: x[-1], max_)
    min_peaks = map(lambda x: [x[0], x[1]], min_)
    min_fitted = map(lambda x: x[-1], min_)
    return [max_peaks, min_peaks]
    
    
def peakdetect_sine_locked(y_axis, x_axis, points = 9):
    """
    Convinience function for calling the 'peakdetect_sine' function with
    the lock_frequency argument as True.
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find peaks
    x_axis -- A x-axis whose values correspond to the y_axis list and is used
        in the return to specify the postion of the peaks.
    points -- (optional) How many points around the peak should be used during
        curve fitting, must be odd (default: 9)
        
    return -- see 'peakdetect_sine'
    """
    return peakdetect_sine(y_axis, x_axis, points, True)
    
    
def peakdetect_zero_crossing(y_axis, x_axis = None, window = 11):
    """
    Function for detecting local maximas and minmias in a signal.
    Discovers peaks by dividing the signal into bins and retrieving the
    maximum and minimum value of each the even and odd bins respectively.
    Division into bins is performed by smoothing the curve and finding the
    zero crossings.
    
    Suitable for repeatable signals, where some noise is tolerated. Excecutes
    faster than 'peakdetect', although this function will break if the offset
    of the signal is too large. It should also be noted that the first and
    last peak will probably not be found, as this function only can find peaks
    between the first and last zero crossing.
    
    keyword arguments:
    y_axis -- A list containg the signal over which to find peaks
    x_axis -- (optional) A x-axis whose values correspond to the y_axis list
        and is used in the return to specify the postion of the peaks. If
        omitted an index of the y_axis is used. (default: None)
    window -- the dimension of the smoothing window; should be an odd integer
        (default: 11)
    
    return -- two lists [max_peaks, min_peaks] containing the positive and
        negative peaks respectively. Each cell of the lists contains a tupple
        of: (position, peak_value) 
        to get the average peak value do: np.mean(max_peaks, 0)[1] on the
        results to unpack one of the lists into x, y coordinates do: 
        x, y = zip(*tab)
    """
    x_axis, y_axis = _datacheck_peakdetect(x_axis, y_axis)
    zero_indices = zero_crossings(y_axis, window = window)
    period_lengths = np.diff(zero_indices)
    
    bins_y = [y_axis[index:index + diff] for index, diff in zip(zero_indices, period_lengths)]
    bins_x = [x_axis[index:index + diff] for index, diff in zip(zero_indices, period_lengths)]
    
    even_bins_y = bins_y[::2]
    odd_bins_y = bins_y[1::2]
    even_bins_x = bins_x[::2]
    odd_bins_x = bins_x[1::2]
    hi_peaks_x = []
    lo_peaks_x = []
    
    if abs(even_bins_y[0].max()) > abs(even_bins_y[0].min()):
        hi_peaks = [bin.max() for bin in even_bins_y]
        lo_peaks = [bin.min() for bin in odd_bins_y]
        for bin_x, bin_y, peak in zip(even_bins_x, even_bins_y, hi_peaks):
            hi_peaks_x.append(bin_x[np.where(bin_y==peak)[0][0]])
        for bin_x, bin_y, peak in zip(odd_bins_x, odd_bins_y, lo_peaks):
            lo_peaks_x.append(bin_x[np.where(bin_y==peak)[0][0]])
    else:
        hi_peaks = [bin.max() for bin in odd_bins_y]
        lo_peaks = [bin.min() for bin in even_bins_y]
        for bin_x, bin_y, peak in zip(odd_bins_x, odd_bins_y, hi_peaks):
            hi_peaks_x.append(bin_x[np.where(bin_y==peak)[0][0]])
        for bin_x, bin_y, peak in zip(even_bins_x, even_bins_y, lo_peaks):
            lo_peaks_x.append(bin_x[np.where(bin_y==peak)[0][0]])
    
    max_peaks = [[x, y] for x,y in zip(hi_peaks_x, hi_peaks)]
    min_peaks = [[x, y] for x,y in zip(lo_peaks_x, lo_peaks)]
    
    return [max_peaks, min_peaks]


def _datacheck_peakdetect(x_axis, y_axis):
    """
    Needed function in order to use peackdetect
    Basically it checks if the x_axis and y_axis are of the right type and lenght 
    
    Args:
        x_axis, y_axis: array of numbers where y(x)
    
    Returns: 
        x_axis, y_axis: if they are correct and in the right shape
    
    """
    if x_axis is None:
        x_axis = range(len(y_axis))
    
    if len(y_axis) != len(x_axis):
        raise (ValueError, 'Input vectors y_axis and x_axis must have same length')
    
    y_axis = np.array(y_axis)
    x_axis = np.array(x_axis)
    return x_axis, y_axis


def _peakdetect_parabole_fitter(raw_peaks, x_axis, y_axis, points):
    """
    Needed function in order to use peackdetect
    Performs the actual parabole fitting for the peakdetect_parabole function.
    
    keyword arguments:
    raw_peaks -- A list of either the maximium or the minimum peaks, as given
        by the peakdetect_zero_crossing function, with index used as x-axis
    x_axis -- A numpy list of all the x values
    y_axis -- A numpy list of all the y values
    points -- How many points around the peak should be used during curve
        fitting, must be odd.
    
    return -- A list giving all the peaks and the fitted waveform, format:
        [[x, y, [fitted_x, fitted_y]]]
        
    """
    func = lambda x, k, tau, m: k * ((x - tau) ** 2) + m
    fitted_peaks = []
    for peak in raw_peaks:
        index = peak[0]
        x_data = x_axis[index - points // 2: index + points // 2 + 1]
        y_data = y_axis[index - points // 2: index + points // 2 + 1]
        tau = x_axis[index]
        m = peak[1]
        
        p0 = (-m, tau, m)
        popt, pcov = curve_fit(func, x_data, y_data, p0)
        x, y = popt[1:3]
        
        x2 = np.linspace(x_data[0], x_data[-1], points * 10)
        y2 = func(x2, *popt)       
        fitted_peaks.append([x, y, [x2, y2]])
        
    return fitted_peaks
	
	

def interactivepeak(data):
	"""
	FUNNY GRAPHICAL INTERFACE for finding the peaks! ;)
	
	Author: Michele Monti
	
	Args:
		data: is a data set x,y
	
	Returns: plot the data and for each clic point a maximum of the graph! 
	"""
		X,Y = data[:,0], data[:,1]
		fig = plt.figure()
		ax = fig.add_subplot(111)
		ax.plot(X,Y,label = "prova")
		plt.xlim(min(X) * 0.9, max(X) * 1.1)
		plt.ylim(min(Y) * 0.9, max(Y) * 1.1)
		plt.ylabel(r'Y axis')
		plt.xlabel(r'X axis')
		diz = dict(zip(X, Y))
		interval = []
		peaks_list = []
		
		def onclick(event):
			print 'First limit at =%f'%(event.xdata)
			interval.append(event.xdata)
			if len(interval) % 2 == 0:
				pos_a = interval[-2]     
				pos_b = interval[-1]
				if pos_b < pos_a: A = pos_b; B = pos_a
				else: A = pos_a; B = pos_b
				peak_y = 0
				picco_x = 0
				for i in [ j for j in X if A < j < B] :
					if diz[i] > peak_y:
						peak_y = diz[i]
						picco_x = i
				print "Interval: %f - %f  Peak at: %f " %(a, b, picco_x)
				peaks_list.append([picco_x, peak_y])
				ax.annotate("picco", xy = (picco_x, peak_y),  xycoords = 'data',
						xytext = (-50, 30), textcoords = 'offset points',
						arrowprops = dict(arrowstyle="->"))
			plt.draw()

		cid = fig.canvas.mpl_connect('button_press_event', onclick)	
		return plt.show()     

		
def datamaxmin(file_name,x_column = 0, y_column = 1, graph = False):
	"""
	
	Args:
		file_name: is the name of the data file to analyze. It has to be .txt. 
		x_column: is the column of the data file to se as the x axis 
		y_column: is the column that hat to set as yaxis		
		graph: set True if you want to plot the data with maxima and minima.
		
	Returns:
		maxima: list of the maximal y-coordinates, with corresponding x-value (maxima[:,0])
		minima: list of the minimal y-coordinates, with corresponding x-value (mimima[:,0])
	
	"""
	
	data = np.loadtxt(file_name)
	t, y = data[:,x_column], data[:,y_column]
	list_t = list(t)
	list_y = list(y)
	maxima, minima = peakdetect(list_y, x_axis = list_t)
	if graph:
		plt.plot(list_t, list_y)
		plt.plot(maxima[:,0], maxima[:,1], "o")
		plt.plot(minima[:,0], minima[:,1], "o")
		plt.show()
	
	return maxima, minima