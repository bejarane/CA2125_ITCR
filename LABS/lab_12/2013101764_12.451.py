# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 12.451
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
    archivo = open(input("Digite el nombre del archivo: "),"r")
    cuantos = len(archivo.read())
    archivo.close()
    print("El archivo tiene %i caracteres" % cuantos)

except FileNotFoundError:
    print("Error: el archivo no existe.")
