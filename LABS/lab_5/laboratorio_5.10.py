# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.10
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



string = input("Digite su texto sin mayusculas: ")

while not (string == "-2"):
    
    if(string.islower()):
        print("Aprueba")
        break
    print("Error, mayuscula en texto")
    
        
    string = input("Digite su texto sin mayusculas: ")
