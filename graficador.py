import matplotlib.pyplot as plt

import metodoEuler
import metodoRungeKutta

def graficar(titulo, dominio, imagen, x1, y1, x2, y2):

	plt.plot(x1, y1, linewidth=0, color='c', marker='*')
	plt.plot(x2, y2, linewidth=0, color='b', marker='o')

	plt.xlabel(dominio)
	plt.ylabel(imagen)
	plt.grid()
	plt.show()
	plt.savefig(titulo + ".png")



def main():
	posEuler, velEuler, acelEuler, tiempoEuler = metodoEuler.euler(0.002, 0, 0)
	posRK4, velRK4, acelRK4, tiempoRK4 = metodoRungeKutta.rungekutta4(0.1, 0, 0)

	graficar("grafico _posicion", "tiempo", "posicion", tiempoEuler, posEuler, tiempoRK4, posRK4)
	graficar("grafico _velocidad", "tiempo", "velocidad", tiempoEuler, velEuler, tiempoRK4, velRK4)
	graficar("grafico _aceleracion", "tiempo", "aceleracion", tiempoEuler, acelEuler, tiempoRK4, acelRK4)



main()