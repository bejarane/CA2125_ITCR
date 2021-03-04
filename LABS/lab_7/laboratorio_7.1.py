# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 7.1
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

matriz2 = []
for i in range(dimension):
    matriz2.append([0]*dimension)
print("Triangular superior")
for r in range(dimension):
    for c in range(r, dimension):
        matriz2[r][c] = matriz[r][c]
for r in range(dimension):
    print(matriz2[r])

matriz2 = []
for i in range(dimension):
    matriz2.append([0]*dimension)
print("Triangular inferior")
for r in range(dimension):
    for c in range(r+1):
        matriz2[r][c] = matriz[r][c]
for r in range(dimension):
    print(matriz2[r])
