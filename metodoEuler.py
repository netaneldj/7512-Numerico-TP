import math

def euler(a,b,N,y0):
	h=calcularPaso(a,b,N)
	y = []
	y.append(y0)
	for i in range(N):
		y.append(y[i] + h*f(calcularPunto(a,i,h),y[i]))
	return y[N]
		
def calcularPaso(a,b,N):
	return float(b-a)/N

def calcularPunto(a,i,h):
	return a+i*h

def f(t,y):
	return y-t*t+1

def main():
	print(euler(0,2,4,0.5))

main()
