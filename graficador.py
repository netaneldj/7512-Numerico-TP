import matplotlib.pyplot as plt

import metodoEuler
import metodoRungeKutta

KMH = 3.6
G = 9.807

def graficar(n, titulo, dominio, imagen, x1, y1, x2, y2):

	if (n==2):
		plt.plot(x1, y1, linewidth=1, color='c')#, marker='*')

	plt.plot(x2, y2, linewidth=1, color='b')#, marker='o')

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

	graficar(2, "grafico _posicion", "tiempo (s)", "posicion (m)", tiempoEuler, posEuler, tiempoRK4, posRK4)

	graficar(2, "grafico _velocidad", "tiempo (s)", "velocidad (km/h)", tiempoEuler, cambio_unidades_velocidad(velEuler),
			 tiempoRK4, cambio_unidades_velocidad(velRK4))
	graficar(2, "grafico _aceleracion", "tiempo (s)", "aceleracion (g)", tiempoEuler, cambio_unidades_aceleracion(acelEuler),
			 tiempoRK4, cambio_unidades_aceleracion(acelRK4))

def grafico_simple():
	y, v, a, t = metodoRungeKutta.rungekutta4(0.002, 0, 0)
	graficar(1, "grafico _posicion", "tiempo (s)", "posicion (m)", None, None,  t, y)
	graficar(1, "grafico _velocidad", "tiempo (s)", "velocidad (km/h)", None, None, t, cambio_unidades_velocidad(v))
	graficar(1, "grafico _aceleracion", "tiempo (s)", "aceleracion (g)", None, None, t, cambio_unidades_aceleracion(a))

def main():

	grafico_comparativo()
	#grafico_simple()



main()
