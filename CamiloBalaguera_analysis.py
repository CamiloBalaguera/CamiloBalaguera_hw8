import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def normal_dist(x, mean, sigma):
	z = np.array(x)
	z = (z/np.std(z))*sigma
	z = (z-np.mean(z)) + mean
	return z

def get_fit(filename):
	a = np.genfromtxt(filename, usecols=0)
	np.histogram(a)
	plt.hist(a, bins='auto')
	plt.show()
	popt, pcov = curve_fit(normal_dist, xdata, ydata)

	
	


