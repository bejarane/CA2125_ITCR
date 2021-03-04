# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.9
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

lista = ['a','e','i','o','u']

while not (string == "-2"):
    str1 = string.upper();
    str2 = string.lower();

    if(str1 == str2):
        print("Es otro tipo de caracter")
    elif (string in lista):
        print("Es vocal minuscula")
    elif(str2 in lista):
        print("Es vocal mayuscula")
    elif(string == str1):
        print("Es consonante mayuscula")
    elif(string == str2):
        print("Es consonante minuscula")
    
        
    string = input("Digite su caracter: ")
