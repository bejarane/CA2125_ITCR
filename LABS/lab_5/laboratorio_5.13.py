# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.13
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
##requiere quitar espacio y caracteres no alfabeticos

##ruta natural no es palindromo, la ruta natural si


string = input("Digite su palindromo: ")
result = ""
for char in string: ##remueve espacios  para que solo valgan los caracteres
    if (char.isalpha()):
        result += char
string = result

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
    
