import math

ERROR = math.pow(5,-17)
#PADRON = 99093
#L0 = 2*100000/PADRON
L0 = 2.02 #Redondeado a 3 digitos significativos
G = 9.81
K = 10
M = 0
A = 1

def punto_fijo(g,inicio,fin,error):
	raiz = []
	verificar_acotada(g,inicio,fin)
	verificar_acotada(derivadaG,inicio,fin)
	comienzo = calcular_comienzo(inicio,fin)
	if(punto_fijo_rec(g,comienzo,error,raiz)):
		return raiz
	raise ValueError("No hay raiz")
		
def punto_fijo_rec(g,comienzo,error,raiz):
	raiz.append(comienzo)
	if(abs(f(comienzo))<=ERROR):
		return True
	medio = g(comienzo)
	punto_fijo_rec(g,medio,error,raiz)
	return True

def verificar_pertenencia_intervalo(g,inicio,fin):
	return (inicio<=g(inicio)<=fin and inicio<=g(fin)<=fin)

def verificar_acotada(derivadaG,inicio,fin):
	return (derivadaG(inicio)<=1 and derivadaG(fin)<=1) 

def calcular_comienzo(inicio,fin):
	return (inicio+fin)/2

def f(y):
	return -2*K*y*(1-L0/math.sqrt(y*y+A*A))-M*G 
	
def g(y):
	return y*L0/math.sqrt(y*y+A*A) - M*G/(2*K)

def derivadaG(y):
	return (L0*math.sqrt(y*y+A*A)-L0*y*y/math.sqrt(y*y+A*A))/(y*y+A*A)

def main():
	print(punto_fijo(g,1,2,ERROR))

main()
