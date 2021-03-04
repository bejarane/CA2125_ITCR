# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.8
#
#   FECHA: 11/04/20
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



string = input("Digite su caracter: ")

while not (string == "-2"):
    if (string.isalpha()):
        if (string.isupper()):
            print("Es una MAYUSCULA")
        else:
            print("Es una MINUSCULA")
    else:
        print("No es una letra")
    string = input("Digite su caracter: ")


##metodo 2 sin is alpha
string = input("Digite su caracter: ")

while not (string == "-2"):
    ##sin utilizar swapcase
    strup = string.upper()
    strdn = string.lower()
    if (strup!=strdn): ##los caracteres no alfabeticos no son afectados por upper y lower
        if (string.isupper()):
            print("Es una MAYUSCULA")
        else:
            print("Es una MINUSCULA")
    else:
        print("No es una letra")
    string = input("Digite su caracter: ")
    

