# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio Virtual 4.26
#
#   FECHA: 5/05/20
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

##funciones

def factorial(numero):
    factorial = 1
    for n in range(1,numero+1):
        factorial *= n
    return factorial
#programa
x = int(input("Ingrese un numero entero: "))
print(factorial(x))
