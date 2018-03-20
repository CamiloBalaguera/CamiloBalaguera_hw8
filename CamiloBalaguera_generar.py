import numpy as np

#Funcion que retorna distribución discreta.
def sample_1(N):
	return np.random.choice(a = [-10, -5, 3, 9],size = N, p=[0.1, 0.4, 0.2, 0.3])

#Funcion que retorna distribución exponencial con Beta 0.5
def sample_2(N):
	return np.random.exponential(0.5, N)

#Funcion que retorna M numero de promedios dada una funcion de sampleo.
def get_mean(sampling_fun, N, M):
	prom = []
	for i in range(0, M):
		prom.append(np.mean(sampling_fun(N)))
	prom = np.array(prom)
	return prom

tamaño = 10000 #Tamaño M establecido por el ejercicio
Numeros = [10, 100, 1000] #Lista con los valores posibles de la variable N

# Iteración que me genera todos los archivos de texto con el Output de get_mean
for i in range(len(Numeros)):
	sp1 = "sample_1_"+str(Numeros[i])+".txt"
	sp2 = "sample_2_"+str(Numeros[i])+".txt"
	np.savetxt(sp1, get_mean(sample_1, Numeros[i], tamaño))
	np.savetxt(sp2, get_mean(sample_2, Numeros[i], tamaño))
		
