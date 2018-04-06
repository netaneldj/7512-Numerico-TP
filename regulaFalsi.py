import math

ERROR = math.pow(5,-17)
#PADRON = 99093
#L0 = 2*100000/PADRON
L0 = 2.02 #Redondeado a 3 digitos significativos
G = 9.81
K = 10
M = 0
A = 1

def regula_falsi(f,inicio,fin,error):
	raiz = []
	if(regula_falsi_rec(f,inicio,fin,error,raiz)):
		return raiz[0]
	raise ValueError("No hay raiz")	
	
def regula_falsi_rec(f,inicio,fin,error,raiz):
	medio = calcular_medio(f,inicio,fin)
	if(abs(f(inicio))<=error or abs(f(medio))<=error or abs(f(fin))<=error):
		raiz.append(medio)
		return True
	if(f(inicio)*f(medio)>0 and f(medio)*f(fin)>0):
		return False
	if(f(inicio)*f(medio)<0):
		regula_falsi_rec(f,inicio,medio,error,raiz)
	regula_falsi_rec(f,medio,fin,error,raiz)
	return True	
	
def calcular_medio(f,inicio,fin):
	return (fin*f(inicio)-inicio*f(fin))/(f(inicio)-f(fin))

def verificar_intervalo(f,inicio,fin):
	if((f(inicio)>0 and f(fin)>0) or (f(inicio)<0 and f(fin)<0)):
		raise Exception("Intervalo invalido")

def f(y):
	return -2*K*y*(1-L0/math.sqrt(y*y+A*A))-M*G 
	
def main():
	print(regula_falsi(f,1,2,ERROR))

main()
