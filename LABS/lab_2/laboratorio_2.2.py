# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.2
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

import random

aPagar = int(input("Indique el total de la compra: "))

loteria = random.randint(1,100)

if loteria < 50:
    print("El descuento de un 15 porciento es:", aPagar*0.15)
else:
    print("El descuento de un 20 porciento es:", aPagar*0.2)
