# coding=utf-8
#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 1.6
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


lado = eval(input("Indique el lado del cuadrado: ")) ##eval interpreta el string como si fuera codigo https://www.tutorialspoint.com/python-eval

per = lado * 4
area = lado**2


print("Perimetro: ",per," m",", Area: ",area," m²")
