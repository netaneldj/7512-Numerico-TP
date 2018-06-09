import math

G = 9.807
M = 87.464
L0 = 51.549
K1 = 49.366
K2 = 1

def rungekutta(h,y0,f,v0,t):
	q1 = h*f(y0)
	q2 = f(y0+(q1/2)*(t+h/2))
	q3 = f(y0+(q2/2)*(t+h/2))
	q4 = f(y0+q3*(t+h))
	return v0+(q1+2*q2+2*q3+q4)*h/6
	
	'''q1 = f(y0)
	q2 = v0+(h/2)*f(y0)
	q3 = v0+(h/2)*f(y0+v0*(h/2)+(1/2)*f(y0)*(h*h/4))
	q4 = v0+h*f(y0+v0*(h/2)+(1/2)*f(y0)*(h*h/4))
	return v0+(h/6)*(q1+2*q2+2*q3+q4)'''

def aplicacion(h, y0, v0,t):

	posicion = []
	posicion.append(y0)

	velocidad = []
	velocidad.append(v0)

	aceleracion = []
	aceleracion.append(calcular_aceleracion(y0))

	oscilacion = 0
	n = 0
	t = 0
	cuarta_oscilacion = False

	#while not cuarta_oscilacion:
	for i in range(50):
		posicion.append(calcular_posicion(posicion, velocidad, h, n,t))
		velocidad.append(calcular_velocidad(posicion, velocidad, h,n,t))
		aceleracion.append(calcular_aceleracion(posicion[n+1]))

		n+=1
		t+=n*h

		'''if hay_un_maximo(posicion, n):
			oscilacion+=1
			if oscilacion == 4:
				cuarta_oscilacion = True'''
				
	print("!!!POSICION!!!!")
	print(posicion)
	print("!!!VELOCIDAD!!!")
	print(velocidad)
	print("!!!ACELERACION!!!")
	print(aceleracion)

def calcular_posicion(y, v, h, n,t):
	return y[n]+h*calcular_velocidad(y,v,h,n,t)

def calcular_velocidad(y, v, h, n,t):
	return v[n] + rungekutta(h,y[n],calcular_aceleracion,v[n],t)

def calcular_aceleracion(y):
	if (y < L0): return G
	return G - (K1/M) * math.pow(y-L0, K2)

def hay_un_maximo(y, n):
	if (n > 1) and (y[n] > y[n-1]) and (y[n-1] < y[n-2]): return True
	return False

def main():
	aplicacion(0.1,0,0,0) # intervalo h, posicion inicical, velocidad inicial

main()
