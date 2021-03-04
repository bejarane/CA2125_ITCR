# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.4
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

try:
    numero = int(input("Digite el numero a evaluar: "))

    evalN = numero%2

    if evalN ==0:
        print("Numero par")
    else:
        print("Numero impar")
        
except ValueError:
    print("Error de entrada. Valor no reconocido: ValueError")

    
   
