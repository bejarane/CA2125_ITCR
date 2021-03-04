# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.18
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
cadena = input("Digite una serie de palabras separadas por un espacio: ")
k = int(input("Digite un numero entero: "))
lista = cadena.split()

palabras = len(lista)

eqK = 0
gtK = 0
ltK = 0

caracteres = 0

for j in lista:
    if len(j) == k:
        eqK += 1
##    elif len(j) < k:
##        ltK += 1
    else:
        gtK += 1

##caso especial para la ultima letra que no tiene espacio al final
##y ocurre al finalizar el for

print("Palabras con longitud de %d caracteres: %d" % (k,eqK))
if eqK > 0:
    print("Hay palabras con exactamente %d caracteres" % k)
else:
    print("Ninguna palabra tiene %d caracteres" % k)

if eqK == palabras:
    print("Todas las palabras tienen %d caracteres" % k)
else:
    print("No todas las palabras tienen %d caracteres" % k)

if gtK > 0:
    print("Hay palabras mas largas que %d caracteres" % k)
else:
    print("No hay palabras mas largas que %d caracteres" % k)

##if ltK > 0:
##    print("Hay palabras mas cortas que %d caracteres" % k)
##else:
##    print("No hay palabras mas cortas que %d caracteres" % k)
