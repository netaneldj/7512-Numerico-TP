import matplotlib.pyplot as plt

import metodoEuler
import metodoRungeKutta
import metodoRungeKuttaAire

KMH = 3.6
G = 9.807

def graficar(n, titulo, dominio, imagen, x1, y1, x2, y2, x3, y3):
	
	if(n==3):
		plt.plot(x2, y2, linewidth=1, color='b')#, marker='*') Runge Kutta 4!
		plt.plot(x3,y3,linewidth=1,color='r') #Runge-Kutta 4 Restriccion aceleracion!
	
	if (n==2):
		plt.plot(x2, y2, linewidth=1, color='b')#, marker='*') 

	plt.plot(x1, y1, linewidth=1, color='c')#, marker='o') Euler!

	plt.xlabel(dominio)
	plt.ylabel(imagen)
	plt.grid()
	plt.show()

def cambio_unidades_velocidad (velocidad):
	v = []
	for x in velocidad:
		v.append(x*KMH)
	return v

def cambio_unidades_aceleracion(aceleracion):
	a = []
	for x in aceleracion:
		a.append(x/G)
	return a

def grafico_comparativo():
	posEuler, velEuler, acelEuler, tiempoEuler = metodoEuler.euler(0.002, 0, 0)
	posRK4, velRK4, acelRK4, tiempoRK4 = metodoRungeKutta.rungekutta4(0.002, 0, 0)
	posRKA4, velRKA4, acelRKA4, tiempoRKA4 = metodoRungeKuttaAire.rungekutta4(0.002, 0, 0)
	
	graficar(3, "grafico _posicion", "tiempo (s)", "posicion (m)", tiempoRKA4, posRKA4, tiempoRK4, posRK4, tiempoEuler, posEuler)

	graficar(3, "grafico _velocidad", "tiempo (s)", "velocidad (km/h)", tiempoRKA4, cambio_unidades_velocidad(velRKA4),
			 tiempoRK4, cambio_unidades_velocidad(velRK4), tiempoEuler, cambio_unidades_velocidad(velEuler))
	graficar(3, "grafico _aceleracion", "tiempo (s)", "aceleracion (g)", tiempoRKA4, cambio_unidades_aceleracion(acelRKA4),
			 tiempoRK4, cambio_unidades_aceleracion(acelRK4), tiempoEuler, cambio_unidades_aceleracion(acelEuler))

	
	'''graficar(2, "grafico _posicion", "tiempo (s)", "posicion (m)", tiempoEuler, posEuler, tiempoRK4, posRK4)

	graficar(2, "grafico _velocidad", "tiempo (s)", "velocidad (km/h)", tiempoEuler, cambio_unidades_velocidad(velEuler),
			 tiempoRK4, cambio_unidades_velocidad(velRK4))
	graficar(2, "grafico _aceleracion", "tiempo (s)", "aceleracion (g)", tiempoEuler, cambio_unidades_aceleracion(acelEuler),
			 tiempoRK4, cambio_unidades_aceleracion(acelRK4))'''

def grafico_simple():
	y, v, a, t = metodoRungeKutta.rungekutta4(0.002, 0, 0)
	graficar(1, "grafico _posicion", "tiempo (s)", "posicion (m)", None, None,  t, y)
	graficar(1, "grafico _velocidad", "tiempo (s)", "velocidad (km/h)", None, None, t, cambio_unidades_velocidad(v))
	graficar(1, "grafico _aceleracion", "tiempo (s)", "aceleracion (g)", None, None, t, cambio_unidades_aceleracion(a))

def main():

	grafico_comparativo()
	#grafico_simple()



main()
