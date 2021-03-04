# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio Virtual 4.20
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

def maxcd(a,b):
    a = min(a,b)
    b = max(a,b)

    divisor = 0

    if b==a:
        return 0
    elif b%a == 0:
        return a
    else:
        for j in range(1,b+1):
            if (a%j==0 and b%j==0):
                divisor = j
        return divisor
            

#programa
n = int(input("Ingrese a: "))
m = int(input("Ingrese b: "))
print(maxcd(n,m))
