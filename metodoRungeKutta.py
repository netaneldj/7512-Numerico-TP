import math
NP = 99366
G = 9.8
K1 = 49.366 
M = 87.464
L0 = 51.549
U0 = 0

def rungekutta(un0,h,f,t=0):
	q1 = h*f(un0,t)
	q2 = h*f(un0+q1/2,h/2)
	q3 = h*f(un0+q2/2,t+h/2)
	q4 = h*f(un0+q3,t+h)
	return un0+(q1+2*q2+2*q3+q4)/6
	 	

def fu(vn,t):
	return float(vn)

def fv(un,t):
	if(un>L0):
		return float(G-(K1/M)*(un-L0))
	return G
	
def main():
	lu = []
	lv = []
	lu.append(U0)
	for i in range(100):
		aux = rungekutta(lu[i],0.1,fv)
		lv.append(aux)
		lu.append(rungekutta(aux,0.1,fu))
	print("!!!POSICION!!!!")
	print(lu)
	print("!!!!VELOCIDAD!!!!")
	print(lv)
main()
