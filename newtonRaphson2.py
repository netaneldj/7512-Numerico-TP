import math

ERROR = math.pow(5, -17)  # De esta forma el resultado queda con 16 digitos significativos
VACIO = None #Valor de inicio que nunca puede ser el error para que no queden defasados los K
# PADRON = 99093
# L0 = 2*100000/PADRON
L0 = 2.02  # Redondeado a 3 digitos significativos
G = 9.81
K = 10
M = 0
A = 1

def newton_raphson(f, inicio, fin, error):
	raiz = []
	absError = []
	relError = []
	k = 0
	semilla = fin
	raiz.append(semilla)
	newton_raphson_rec(f, derivada, semilla, raiz, absError, relError, k)

	print raiz
	print absError
	print relError
	p = calcular_exp_p(absError)
	print p
	print calcular_lambda(absError, p)
	
def newton_raphson_rec(f, derivada, comienzo, raiz, errorAbs, errorRel, k):
	punto = calcular_proximo_punto(f, derivada, comienzo)
	raiz.append(punto)
	errorAbs.append(abs(raiz[k+1]-raiz[k]))
	errorRel.append(abs(errorAbs[k]/(raiz[k])))
	if errorRel[k] < ERROR:
		return
	k+=1
	newton_raphson_rec(f, derivada, punto, raiz, errorAbs, errorRel, k)

	
def calcular_proximo_punto(f, derivada, xn):
	return xn-f(xn)/derivada(xn)

def f(y):
	return -2*K*y*(1-L0/math.sqrt(math.pow(y, 2)+math.pow(A, 2)))-M*G

def derivada(y):
	return -2*K + (2*K*L0/math.sqrt(math.pow(y,2)+math.pow(A,2)))*(1-math.pow(y,2)/(math.pow(y,2)+math.pow(A,2)))

def calcular_exp_p(absE):
	p = []
	for k in range(len(absE)):
		if k > 1:
			try:
				p.append(math.log((absE[k+1]/absE[k]), math.e) / math.log((absE[k]/absE[k-1]), math.e)) #Da error porque el error absoluto en la posicion K da cero
			except:
				p.append(p[k-1])
		else:
			p.append(VACIO)
		k+=1
	return p

def calcular_lambda(absE, p):
	y = []
	for k in range(len(absE)):
		if k > 1:
			print(absE[k],absE[k-1], p[k])
			y.append(absE[k] / math.pow(absE[k-1], p[k]))
		else:
			y.append(VACIO)
		k+=1
	return y

def main():
	newton_raphson(f, 1, 2, ERROR)

main()

