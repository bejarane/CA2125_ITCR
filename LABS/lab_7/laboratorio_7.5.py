# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 7.5
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

for x in range(dimension):
    matriz[x][x] = 1

for j in matriz:
    print(j)
