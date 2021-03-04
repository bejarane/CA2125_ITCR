# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.7
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

    menor = 0
    mayor = 0

    menor = numero1
    mayor = numero1

    if numero2 <= menor:  ##un numero es menor o igual cuando hay un empate
        menor = numero2
    elif numero2 >= mayor:
        mayor = numero2

    if numero3 <= menor:  ##un numero es menor igual cuando hay un empate
        menor = numero3
    elif numero3 >= mayor:
        mayor = numero3

    if numero4 <= menor:  ##un numero es menor igual cuando hay un empate
        menor = numero4
    elif numero4 >= mayor:
        mayor = numero4

    if numero5 <= menor:  ##un numero es menor igual cuando hay un empate
        menor = numero5
    elif numero5 >= mayor:
        mayor = numero5

  

    print("El numero menor es: ",menor," y el mayor: ",mayor)


except ValueError:
    print("Error de entrada. Valor no reconocido: ValueError")
    
   
