# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.3
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
#//////////////////Fucion Principal///////////////////////#
###########################################################

import math

vX = int(input("Digite el valor de X: "))

evalX = vX%4

if evalX ==0:
    print("f(x) = x*x =>", vX**2)
elif evalX == 1:
    print("f(x) = x/6 =>", vX/6)
elif evalX == 2:
    print("f(x) = sqrt(x) =>", math.sqrt(vX))
elif evalX == 3:
    print("f(x) = x*x*x+5 =>", vX**3 +5)
   
