# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.4
#
#   FECHA: 14/05/20
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

##si evaluando cada char del string con int(),
##pero en caso que sea una letra requiere de un trycatch.
##utilizare la funcion integrada in de listas. No sé si se debía utilizar
##una estructura de control con if, elif, else.

string = input("Digite una cadena de texto: ")
resultado = ""

for char in string:
    if (char in lista):
        resultado += char

if (len(resultado)==0):
    print(0)
else:
    print("Procesado: ", resultado)

