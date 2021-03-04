# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 1.2
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



num1 = int(83472)
d1 = num1 // 10000 ##realiza una division entera
residuo = num1 % 10000 ##calcula el residuo de una division entera

d2 = residuo // 1000
residuo = residuo %1000

d3 = residuo // 100
residuo = residuo%100

d4 = residuo // 10
residuo = residuo % 10

sp = "   "


print("Numero:",d1,d2,d3,d4,residuo, sep=sp)

