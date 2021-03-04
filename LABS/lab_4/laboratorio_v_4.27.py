# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio Virtual 4.27
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

def combinatoria(n, m):
    if n >= m:
        return (factorial(n)) / (factorial(n-m)*factorial(m))
#programa
n = int(input("Ingrese n: "))
m = int(input("Ingrese m: "))
print(combinatoria(n,m))
