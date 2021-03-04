# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.6
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


numero = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo numero: "))

evalN = numero**2 #se evalua al principio, una unica vez, para reducir futuras operaciones

if evalN == numero2:
    print("El segundo es el cuadrado exacto del primero")
elif evalN < numero2:
    print("El segundo es mayor que el cuadrado del primero")
elif evalN > numero2:
    print("El segundo es menor que el cuadrado del primero")

    
   
