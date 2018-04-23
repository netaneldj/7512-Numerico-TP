import math

ERROR = math.pow(5, -17)  # De esta forma el resultado queda con 16 digitos significativos
VACIO = None
# PADRON = 99093
# L0 = 2*100000/PADRON
L0 = 2.02
G = 9.81
K = 10
# M0 = 100000/PADRON
M0 = 1.01
M = 0*M0
A = 1

def newton_raphson(semilla):
	raiz = []
	absError = []
	relError = []

	raiz.append(semilla)
	absError.append(VACIO)
	relError.append(VACIO)

	k = 1
	newton_raphson_rec(semilla, raiz, absError, relError, k)

	print raiz
	print absError
	print relError
	p = calcular_exp_p(absError)
	print p
	print calcular_lambda(absError, p)
	
def newton_raphson_rec(pto_anterior, raiz, errorAbs, errorRel, k):
	punto = calcular_proximo_punto(pto_anterior)
	raiz.append(punto)

	errorAbs.append(abs(raiz[k]-raiz[k-1]))
	errorRel.append(abs(errorAbs[k]/raiz[k]))

	if errorRel[k] < ERROR:
		return

	k+=1
	newton_raphson_rec(punto, raiz, errorAbs, errorRel, k)

	
def calcular_proximo_punto(xn):
	return xn-f(xn)/derivada(xn)

def f(y):
	return -2*K*y*(1 - L0/math.sqrt(math.pow(y, 2)+math.pow(A, 2))) - M*G

def derivada(y):
	return -2*K*(1 - L0/math.sqrt(math.pow(y,2)+math.pow(A,2))*(1 - math.pow(y,2)/(math.pow(y,2)+math.pow(A,2))))

def calcular_exp_p(absE):
	p = []
	
	for k in range(len(absE)-1):
		if k > 1:
			p.append(math.log((absE[k+1]/absE[k]), math.e) / math.log((absE[k]/absE[k-1]), math.e))

		else:
			p.append(VACIO)

	return p

def calcular_lambda(absE, p):
	y = []

	for k in range(len(absE)-1):
		if k > 1:
			y.append(absE[k+1] / math.pow(absE[k], p[k]))

		else:
			y.append(VACIO)

	return y

def main():
	newton_raphson(1.5)  # el parametro es la semilla

main()

