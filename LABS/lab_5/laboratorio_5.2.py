# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.2
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
longitud = len(string)

medio = int(longitud/2)

for j in range(medio):
    
    print(string[j])
    print(string[-1*(j+1)])

if not (longitud%2==0):
    print(string[medio])

