# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio Virtual 4.21
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

def maxcd(a,b,c):
    mayor = max(a,b,c)
    divisor = 0

    if b==a or b==c:
        return 0
    elif b%a == 0 and c%a == 0:
        return a
    else:
        for j in range(1,mayor+1):
            if (a%j==0 and b%j==0 and c%j==0):
                divisor = j
        return divisor
            

#programa
a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))
print(maxcd(a,b,c))
