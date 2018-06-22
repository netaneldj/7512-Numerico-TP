import math

G = 9.807
M = 87.464
L0 = 51.549
K1 = 21 #49.366 - 9.8 - 21
K2 = 1.1 #1 - 1.25 - 1.1
C1 = 4.873
C2 = 1.5

def ecuacion_iterativa(h, y, v):
    q1y = h*v
    q1v = h*f_aceleracion(y)

    q2y = h*(v + q1v/2)
    q2v = h*f_aceleracion(y + q1y/2)

    q3y = h*(v + q2v/2)
    q3v = h*f_aceleracion(y + q2y / 2)

    q4y = h*(v + q3v)
    q4v = h*f_aceleracion(y + q3y)

    return (y + (q1y + 2*q2y + 2*q3y + q4y)/6), (v + (q1v + 2*q2v + 2*q3v + q4v)/6)

def f_aceleracion (y):
    if y < L0:  return G
    return G - (K1 / M) * math.pow(y - L0, K2)

def f_aceleracion_aire(y,v):
    if y < L0:  return G - (C1 / M) * math.pow(abs(v), C2)
    return G - (K1 / M) * math.pow(y - L0, K2) - (C1 / M) * math.pow(abs(v), C2)

def hay_un_maximo(y, n):
    if (n > 1) and (y[n] < y[n-1]) and (y[n-1] > y[n-2]):   return True
    return False

def rungekutta4 (h, y0, v0):
    posicion = []
    posicion.append(y0)

    velocidad = []
    velocidad.append(v0)

    aceleracion = []
    #aceleracion.append(f_aceleracion(y0))
    aceleracion.append(f_aceleracion_aire(y0, v0))

    oscilacion = 0
    n = 0
    cuarta_oscilacion = False

    tiempo = [0]

    while not cuarta_oscilacion:

        y, v = ecuacion_iterativa(h, posicion[n], velocidad[n])
        posicion.append(round(y, 5))
        velocidad.append(round(v, 5))
    	#aceleracion.append(round(f_aceleracion(y), 5))
        aceleracion.append(round(f_aceleracion_aire(y, v), 5))
        n+=1
        tiempo.append(round(n * h, 3))

        if hay_un_maximo(posicion, n):
            oscilacion += 1

            #print ("{} caida:".format(oscilacion))
            #print ("Pos:{} Vel:{} Acel:{} T:{}".format(posicion[n - 2], velocidad[n - 2], aceleracion[n - 2], tiempo[n - 2]))
            #print ("Pos:{} Vel:{} Acel:{} T:{}".format(posicion[n - 1], velocidad[n - 1], aceleracion[n - 1], tiempo[n - 1]))
            #print ("Pos:{} Vel:{} Acel:{} T:{}".format(posicion[n], velocidad[n], aceleracion[n], tiempo[n]))

            if oscilacion == 4:
                cuarta_oscilacion = True

    return posicion, velocidad, aceleracion, tiempo


def main():
    y, v, a, t = rungekutta4(0.002, 0, 0)  # intervalo h, posicion inicical, velocidad inicial
#    print "posicion: {}".format(y)
#    print "velocidad: {}".format(v)
#    print "aceleracion: {}".format(a)

main()
