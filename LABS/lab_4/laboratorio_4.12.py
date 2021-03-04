# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 4.12
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

n= int(input("Digite el inicio del rango:"))
m = int(input("Digite el final del rango:"))


if (m>n):
    suma = 0
    for g in range(n,m+1):
        suma = suma + g
    print("suma:", suma)     
else:
    print("El valor inicial del rango debe ser mayor al numero final")

