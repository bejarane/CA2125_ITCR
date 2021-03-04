# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 7.4
#
#   FECHA: 04/06/20
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

#funciones
def sumafila(pm,pf):
    suma = 0
    for c in range(len(pm[0])):
        suma += pm[pf][c]
    return suma

def sumacolumna(pm,pc):
    suma = 0
    for f in range(len(pm)):
        suma += pm[f][pc]
    return suma
###############################################

m = [[1,2,4],[2,3,1],[4,1,2]]
m = []

filas = int(input("Digite la cantidad de filas de la matriz: "))
columnas = int(input("Digite la cantidad de columnas de la matriz: "))

for x in range(filas):
    m.append([0]*columnas)

for f in range(filas):
    for c in range(columnas):
        m[f][c] = int(input("Digite el valor (%d,%d): " % (f,c)))

esPrima = True

for f in range(len(m)):
    for c in range(len(m[0])):
        if sumafila(m,f) != sumacolumna(m,c):
            esPrima = False
            break
        ##fin del for
    if not esPrima:
        break

if esPrima:
    print("La matriz es prima")
else:
    print("La matriz no es prima")
