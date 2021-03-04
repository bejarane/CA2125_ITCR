# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Examen pregunta 5
#
#   FECHA: 28/05/20
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

entrada = "hola ola"
busqueda = "hola"

#entrada = input("Ingrese la frase a analizar: ")

##se remueven los caracteres que no interesan para reducir iteraciones
entrada = entrada.lower() ##todo minusculas
entradaL = ""
for i in entrada:
    if i in busqueda:
        entradaL += i

##con un string sin caracteres innecesarios
longitud = len(entradaL)
conteo = 0
pasos = 0
for i in range(longitud):
    ##print("",entradaL[i])
    pasos += 1
    if entradaL[i] == "h":
        for j in range(i+1,longitud): ##i+1 para no revisar de nuevo
            pasos += 1
            ##print("\t",entradaL[j])
            if entradaL[j] == "o":
                for k in range(j+1,longitud):
                    pasos += 1
                    ##print("\t\t",entradaL[k])
                    if entradaL[k] == "l":
                        for l in range(k+1, longitud):
                            pasos += 1
                            ##print("\t\t\t",entradaL[l])
                            if entradaL[l] == "a":
                                conteo = conteo + 1

print("La cadena %s se combina %d veces" %(busqueda,conteo))
