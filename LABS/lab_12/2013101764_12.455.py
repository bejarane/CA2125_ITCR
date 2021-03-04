# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 12.455
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

    larga = lista[0]
    for k in range(1,len(lista)):
        if len(lista[k]) > len(larga):
            larga = lista [k]
    print("La linea más larga es: ")
    print(larga)


except FileNotFoundError:
    print("Error: el archivo no existe.")
