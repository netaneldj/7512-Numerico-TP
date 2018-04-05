import math

def newton_raphson(f,inicio,fin,error):
	verificar_intervalo(f,inicio,fin)
	verificar_derivada(derivada,inicio,fin)
	verificar_doble_derivada(doble_derivada,inicio,fin)
	comienzo = devolver_mismo_signo(doble_derivada,inicio,fin)
	raiz = []
	if(newton_raphson_rec(f,derivada,comienzo,error,raiz)):
		return raiz[0]
	
def newton_raphson_rec(f,derivada,comienzo,error,raiz):
	medio = calcular_medio(f,derivada,comienzo)
	if(abs(f(medio))<=error):
		raiz.append(medio)
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
	
def f(x):
	return x*x*x - x*x + 2 

def derivada(x):
	return 3*x*x -2*x

def doble_derivada(x):
	return 6*x - 2

def mismo_signo(a,b):
	if((a>0 and b>0) or (a<0 and b<0)):
		return True
	return False

def main():
	print(newton_raphson(f,-5,-0.5,0.000002))
main()
