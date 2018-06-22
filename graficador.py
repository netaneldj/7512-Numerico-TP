import matplotlib.pyplot as plt

import metodoEuler
import metodoRungeKutta
import metodoRungeKutta_secundario
import RK4

KMH = 3.6
G = 9.807

def graficar(n, titulo, dominio, imagen, x1, y1, x2, y2):

	if (n==2):
		plt.plot(x1, y1, linewidth=1, color='b')#, marker='*')

	plt.plot(x2, y2, linewidth=1, color='c')#, marker='o')

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
	pos1, vel1, acel1, tiempo1 = RK4.rungekutta4(0.002, 0, 0)
	#pos2, vel2, acel2, tiempo2 = metodoEuler.euler(0.002, 0, 0)
	pos2, vel2, acel2, tiempo2 = metodoRungeKutta_secundario.rungekutta4(0.002, 0, 0)
	
	graficar(2, "grafico _posicion", "tiempo (s)", "posicion (m)", tiempo1, pos1, tiempo2, pos2)

	graficar(2, "grafico _velocidad", "tiempo (s)", "velocidad (km/h)", tiempo1, cambio_unidades_velocidad(vel1),
			 tiempo2, cambio_unidades_velocidad(vel2))
	graficar(2, "grafico _aceleracion", "tiempo (s)", "aceleracion (g)", tiempo1, cambio_unidades_aceleracion(acel1),
			 tiempo2, cambio_unidades_aceleracion(acel2))

def grafico_simple():
	y, v, a, t = metodoRungeKutta.rungekutta4(0.002, 0, 0)
	graficar(1, "grafico _posicion", "tiempo (s)", "posicion (m)",  t, y, None, None)
	graficar(1, "grafico _velocidad", "tiempo (s)", "velocidad (km/h)", t, cambio_unidades_velocidad(v), None, None)
	graficar(1, "grafico _aceleracion", "tiempo (s)", "aceleracion (g)", t, cambio_unidades_aceleracion(a), None, None)

def main():

	grafico_comparativo()
	#grafico_simple()



main()
