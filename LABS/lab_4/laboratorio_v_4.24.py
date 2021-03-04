# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio Virtual 4.24
#
#   FECHA: 7/05/20
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

##funciones

def esPrimo(numero):
    bandera  = 1
    for divisor in range (2, int(math.sqrt(numero)+1)):
        if numero % divisor == 0 and divisor != numero:
            bandera = 0
            break
    return bandera

#programa
n = 1
while n > 0:
    n = int(input("Ingrese un numero a evaluar como primo: "))
    if esPrimo(n) == 1:
        print("El numero es primo")
    else:
        print("El numero no es primo")
