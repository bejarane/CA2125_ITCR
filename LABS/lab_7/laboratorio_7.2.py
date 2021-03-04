# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 7.2
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

dimension = int(input("Indique la cantidad de filas y columnas (cuadrada): "))
matriz = []

for i in range(dimension):
    matriz.append([0]*dimension)

for r in range(dimension):
    for c in range(dimension):
        matriz[r][c] = int(input("Indique el valor %d %d: " % (r,c)))

print("Matriz")
for r in range(dimension):
    print(matriz[r])

bandera = False

for r in range(1,dimension):
    for c in range(r):
        if (matriz[r][c] != 0):
            bandera = True
        ##print(matriz[r][c])
if (not bandera):
    print("La matriz es diagonal superior")
else:
    print("La matriz no es diagonal superior")
