# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.14
#
#   FECHA: 20/05/20
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
charA = 65
chara = 97
totalChar = 25

def cesarE(text,caesar):
    result = ""
    for i in text:
        char = ""
        if i.isupper() and i.isalpha():
            char = ord(i) - charA + caesar
            if char > totalChar:
                char = (char % totalChar) - 1
            char = chr(char+charA)
        elif i.isalpha():
            char = ord(i) - chara + caesar
            if char > totalChar:
                char = (char % totalChar) - 1
            char = chr(char+chara)
        result += char

    return result

text = input("Ingrese un string para encriptar: ")
caesar = int(input("Ingrese la cantidad de pasos: "))
print(cesarE(text,caesar))

text = input("Ingrese un string para desencriptar: ")
caesar = int(input("Ingrese la cantidad de pasos usados: "))
print(cesarE(text,26 - caesar))
