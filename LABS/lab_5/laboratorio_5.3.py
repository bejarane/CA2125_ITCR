# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.3
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

##hacer tarea de los pares restantes

string = input("Digite una cadena de texto: ")
resultado = ""
contador = 0

for char in string:
    if (char == " "):
        contador += 1
    else:
        resultado += char


print("Original: ",string)
print("Procesado: ", resultado)
print("Eliminados ",contador, " espacios en blanco.")

