# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 6.8
#
#   FECHA: 26/05/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
#
#   OBJETIVO: -
#
#   DETALLES: -
#
#   TODO:-
#
#   CAMBIOS:-
#
###########################################################

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################
import math

def distancia(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

n = int(input("Cuantos puntos cartesianos quiere: "))
listaX = []
listaY = []
for i in range(n):
    x = eval(input("Digite la coordenada X: "))
    y = eval(input("Digite la coordenada Y: "))
    listaX.append(x)
    listaY.append(y)
##print (listaX)
##print (listaY)

miX = listaX[1]
miY = listaY[1]
miD = distancia(listaX[0],listaY[0],miX,miY)

for i in range(2,n):
    d = distancia(listaX[0],listaY[0],listaX[i],listaY[i])
    if d < miD:
        miX = listaX[i]
        miY = listaY[i]
        miD = d

print("La coordenada mas cercana a (%d,%d) es (%d,%d)" % (listaX[0],listaY[0],miX,miY))


