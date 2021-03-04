# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.11
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



string = input("Digite su palindromo: ")

long = len(string)

compar = True

cont = 0

while (compar):
    compar = string[cont].upper() == string[-1*(cont+1)].upper()
    if (cont > long/2):
        break
    cont += 1

if (compar):
    print("Es palindromo")
else:
    print("No es palindromo")
    
