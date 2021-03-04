# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 12.453
#
#   FECHA: 14/07/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
########################################################### 

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

try:
    archivo = open(input("Digite el nombre de archivo: "),"r")
    lista = archivo.readlines()
    archivo.close()

    contador = 1
    for k in lista:
        print(contador,k,end="")
        contador += 1

except FileNotFoundError:
    print("Error: el archivo no existe.")
