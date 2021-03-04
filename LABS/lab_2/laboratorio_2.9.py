# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.9
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


try:
    numero1 = int(input("Digite el primer numero: "))
    numero2 = int(input("Digite el segundo numero: "))
    numero3 = int(input("Digite el tercer numero: "))
    numero4 = int(input("Digite el cuarto numero: "))
    numero5 = int(input("Digite el quinto numero: "))

    cercano = numero2

    if abs(numero1-numero3) < abs(numero1-cercano):
        cercano = numero3

    if abs(numero1-numero4) < abs(numero1-cercano):
        cercano = numero4

    if abs(numero1-numero5) < abs(numero1-cercano):
        cercano = numero5
  

    print("El numero mas cercano a: ",numero1, " es: ",cercano)


except ValueError:
    print("Error de entrada. Valor no reconocido: ValueError")
    
   
