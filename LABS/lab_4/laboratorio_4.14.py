# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 4.14
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

suma = 0

if (n%2): ##una unica evaluacion reduce los recursos utilizados en futuros ciclos
    n = n+1

for g in range(n,m+1,2):
    suma = suma + g
print("suma:", suma)     

