# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 12.454
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
archivo = input("Digite el nombre del archivo: ")

try:
    archivo = open(archivo,"r")
    lineas = archivo.readlines()
    palabra = ""
    while palabra != "q":
        palabra = input("Digite una palabra a buscar o ingrese q para salir: ")
        if palabra == "q":
            continue
        contador = 0
        for l in lineas:
            if palabra in l:
                contador += 1
                print(l)
        print("Total de filas con la palabra:",contador)

except FileNotFoundError:
    print("Error: el archivo no existe.")
