# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.8
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

    mayor = numero1

    if numero2 >= mayor:
        mayor = numero2

    if numero3 >= mayor:
        mayor = numero3

    if numero4 >= mayor:
        mayor = numero4

    if numero5 >= mayor:
        mayor = numero5

  

    print("El numero maximo es: ",mayor)


except ValueError:
    print("Error de entrada. Valor no reconocido: ValueError")
    
   
