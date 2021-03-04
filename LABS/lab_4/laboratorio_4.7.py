# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 4.7
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

n= int(input("Digite el inicio del rango(n):"))
m = int(input("Digite el final del rango(m):"))
suma = 0

if (n<=m):
    for g in range(n,m+1):
        suma = suma + g
    print("suma:", suma)    
else:
    print("N debe ser menor o igual que M")

