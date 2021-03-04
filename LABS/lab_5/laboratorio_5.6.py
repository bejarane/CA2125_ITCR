# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.6
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


string = input("Digite su texto: ")

##modo facil
print(string.swapcase())

##modo dificil
resultado = ""

for char in string:
    if (char.isupper()):
        resultado += char.lower()
    else:
        resultado += char.upper()


print("resultado: ",resultado)

