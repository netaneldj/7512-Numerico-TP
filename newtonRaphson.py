import math

ERROR = math.pow(5,-17)
#PADRON = 99093
#L0 = 2*100000/PADRON
L0 = 2.02 #Redondeado a 3 digitos significativos
G = 9.81
K = 10
M = 0
A = 1

def newton_raphson(f,inicio,fin,error):
	verificar_intervalo(f,inicio,fin)
	verificar_derivada(derivada,inicio,fin)
	verificar_doble_derivada(doble_derivada,inicio,fin)
	comienzo = devolver_mismo_signo(doble_derivada,inicio,fin)
	raiz = []
	if(newton_raphson_rec(f,derivada,comienzo,error,raiz)):
		return raiz #[0]
	
def newton_raphson_rec(f,derivada,comienzo,error,raiz):
	medio = calcular_medio(f,derivada,comienzo)
	raiz.append(medio)
	if(abs(f(medio))<=error):
		#raiz.append(medio)
		return True
	newton_raphson_rec(f,derivada,medio,error,raiz)
	return True
	
def calcular_medio(f,derivada,xn):
	return xn-f(xn)/derivada(xn)

def verificar_intervalo(f,inicio,fin):
	if((f(inicio)>0 and f(fin)>0) or (f(inicio)<0 and f(fin)<0)):
		raise Exception("Intervalo invalido")

def verificar_derivada(derivada,inicio,fin):
	try:
		verificar_intervalo(derivada,inicio,fin)
		raise Exception("Se anula la derivada en el intervalo")
	except:
		return
		
def verificar_doble_derivada(doble_derivada,inicio,fin):
	try:
		verificar_intervalo(doble_derivada,inicio,fin)
		raise Exception("Cambia de signo la doble derivada")
	except:
		return
			
def devolver_mismo_signo(f,a,b):
	if(mismo_signo(f(a),a)):
		return a
	return b

def mismo_signo(a,b):
	if((a>0 and b>0) or (a<0 and b<0)):
		return True
	return False
	
def f(y):
	return -2*K*y*(1-L0/math.sqrt(y*y+A*A))-M*G 

def derivada(y):
	return -2*K*(1-L0/math.sqrt(y*y+A*A))-2*K*y*y*L0/math.pow(math.sqrt(y*y+A*A),3)

def doble_derivada(y):
	return 6*K*L0*y*((y*y)/(y*y+A*A)-1)/math.pow(math.sqrt(y*y+A*A),3)

def main():
	print(newton_raphson(f,1,2,ERROR))
main()
