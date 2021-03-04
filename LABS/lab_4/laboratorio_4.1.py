# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 4.2
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

numero = int (input("Digite un numero positivo (negativo para deterse)"))
mayor = numero
menor = numero

while numero>=0:
    print (numero)
    

    if numero > mayor:
        mayor = numero

    if numero < menor:
        menor = numero

    numero = int (input("Digite un numero positivo (negativo para deterse)")) ##se pide al final para almacenarlo y evaluar en la siguiente iteracion

print("el mayor de todos es:", mayor)
print("El menor de todos es:", menor)
print("adios") 
    
    

