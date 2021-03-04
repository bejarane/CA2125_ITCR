# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 4.18
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

##un numero primo no es par
##u numero primo no divide por los primos iniciales
##por debajo de 10 todos primos menos pares y 9
##el numero 1 no es primo por definicion
##

for j in range(1,101):
    if j <= 3 and j>1:
        print (j)
    elif j % 2 == 0 or j == 1:
        continue
    elif j%3 == 0 or j%5==0 or j%7 == 0:
        continue
    elif j < 9:
        print (j)
    else:
        print(j)
