# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 12.452
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
    palabra = input("Digite la palabra a buscar: ")
    contenido = archivo.read()
    archivo.close()

    if palabra in contenido:
        print("La palabra SI se encuentra en el archivo.")
    else:
        print("La palabra NO se encuentra en el archivo.")

except FileNotFoundError:
    print("Error: el archivo no existe.")

