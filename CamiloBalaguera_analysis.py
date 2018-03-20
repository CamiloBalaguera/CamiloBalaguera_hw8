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
	histo = np.histogram(a, normed = true) #Hago un histograma que me retorna las frecuencias y los bins
	plt.hist(a)
	popt, pcov = curve_fit(normal_dist, 0.5*(histo[1][:-1]+histo[1][1:]), histo[0])
	print(filename + str(popt[0]) + str(pcov[0]))

	
	


