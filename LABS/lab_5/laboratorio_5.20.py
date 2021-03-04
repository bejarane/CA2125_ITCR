# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.20
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

def contarN (texto):
    enNumero = False
    contador = 0
    result = ""

    for i in texto:
        if  i.isnumeric():
            if not enNumero:
                enNumero = True
                contador += 1
            result += i
        else:
            enNumero = False

    return contador

texto = input("Ingrese una cadena con valores alfanumericos: ")

print("La cadena contiene",contarN(texto),"numeros.")





            
            
