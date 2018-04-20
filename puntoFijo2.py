import math

ERROR = math.pow(5,-17) #De esta forma el resultado queda con 16 digitos significativos
VACIO = None
#PADRON = 99093
#L0 = 2*100000/PADRON
# M = 0.3*100000/PADRON
L0 = 2.02 #Redondeado a 3 digitos significativos
G = 9.81
K = 10
M = 0.303 # Redondeado a 3 digitos significativos 
A = 1

def punto_fijo(g, inicio, fin, error):
	raiz = []
	absError = []
	relError = []
	k = 1
	semilla = fin
	raiz.append(semilla)
	absError.append(VACIO)
	relError.append(VACIO)
	punto_fijo_rec(k, g, semilla, error, raiz, absError, relError)

	print raiz
	print absError
	print relError
	p = calcular_exp_p(absError)
	print p
	print calcular_lambda(absError, p)

def punto_fijo_rec(k, g, punto, error, raiz, absE, relE):
	proximo_punto = g(punto)
	raiz.append(proximo_punto)
	absE.append(abs(raiz[k]-raiz[k-1]))
	relE.append(abs(absE[k]/raiz[k]))
	if relE[k] < ERROR:
		return
	k+=1
	punto_fijo_rec(k, g, proximo_punto, error, raiz, absE, relE)
	
def g(y):
	return y+2*K*y*(1-L0/math.sqrt(math.pow(y, 2)+math.pow(A, 2)))+M*G
	#return y*L0/math.sqrt(math.pow(y,2)+math.pow(A,2))-M*G/(2*K) #Funcion punto fijo funciona

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
			y.append(absE[k] / math.pow(absE[k - 1], p[k]))
		else:
			y.append(VACIO)
	return y

def main():
	punto_fijo(g,-2,0,ERROR)

main()
