import matplotlib.pyplot as plt

import metodoEuler
import metodoRungeKutta

def graficar(titulo, dominio, imagen, x1, y1, x2, y2):

	#plt.plot(x1, y1, linewidth=1, color='c')#, marker='*')
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
	posRK4, velRK4, acelRK4, tiempoRK4 = metodoRungeKutta.rungekutta4(0.1, 0, 0)

	graficar("grafico _posicion", "tiempo", "posicion", tiempoEuler, posEuler, tiempoRK4, posRK4)

	graficar("grafico _velocidad", "tiempo (s)", "velocidad (km/h)", tiempoEuler, cambio_unidades_velocidad(velEuler),
			 tiempoRK4, cambio_unidades_velocidad(velRK4))
	graficar("grafico _aceleracion", "tiempo (s)", "aceleracion (g)", tiempoEuler, cambio_unidades_aceleracion(acelEuler),
			 tiempoRK4, cambio_unidades_aceleracion(acelRK4))

def grafico_simple():
	y, v, a, t = metodoRungeKutta.rungekutta4(0.001, 0, 0)
	graficar("grafico _posicion", "tiempo", "posicion", t, y,  t, y)
	graficar("grafico _velocidad", "tiempo", "velocidad", t, v, t, v)
	graficar("grafico _aceleracion", "tiempo", "aceleracion", t, a, t, a)

def main():

	#grafico_comparativo()
	grafico_simple()



main()