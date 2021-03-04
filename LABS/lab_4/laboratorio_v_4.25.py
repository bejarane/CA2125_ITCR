# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio Virtual 4.25
#
#   FECHA: 7/05/20
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

import math

##funciones

def reglaAB(numero):
    return (numero + 7) % 10

def codifica(numero):
    ##separar los digitos
    d1 = numero // 10000
    residuo = numero %10000

    d2 = residuo // 1000
    residuo = residuo %1000

    d3 = residuo // 100
    residuo = residuo %100

    d4 = residuo // 10
    d5 = residuo %10

##aplicar las reglas a y b
    d1 = reglaAB(d1)
    d2 = reglaAB(d2)
    d3 = reglaAB(d3)
    d4 = reglaAB(d4)
    d5 = reglaAB(d5)

    if numero >= 10000:
        resultado = d5 * 10000
        resultado += d4*1000
        resultado += d3*100
        resultado += d2*10
        resultado += d1
    elif numero >= 1000:
        resultado = d5*1000
        resultado += d3*100
        resultado += d4*10
        resultado += d2
    elif numero >= 100:
        resultado = d5*100
        resultado += d4*10
        resultado += d3
    elif numero >= 10:
        resultado = d5*10
        resultado += d4
    else:
        resultado = d5

    return resultado

def reglaABI(numero):
    return (numero + 3) % 10

def descodifica(numero):
    ##separar los digitos
    d1 = numero // 10000
    residuo = numero %10000

    d2 = residuo // 1000
    residuo = residuo %1000

    d3 = residuo // 100
    residuo = residuo %100

    d4 = residuo // 10
    
    d5 = residuo %10

    ##aplicar las reglas a y b
    d1 = reglaABI(d1)
    d2 = reglaABI(d2)
    d3 = reglaABI(d3)
    d4 = reglaABI(d4)
    d5 = reglaABI(d5)
    
    if numero >= 10000:
        resultado = d5 * 10000
        resultado += d4*1000
        resultado += d3*100
        resultado += d2*10
        resultado += d1
    elif numero >= 1000:
        resultado = d5*1000
        resultado += d3*100
        resultado += d4*10
        resultado += d2
    elif numero >= 100:
        resultado = d5*100
        resultado += d4*10
        resultado += d3
    elif numero >= 10:
        resultado = d5*10
        resultado += d4
    else:
        resultado = d5

    return resultado


    

#programa
n = 1
while n > 0:
    n = int(input("Codifica: "))
    print(codifica(n))
    n = int(input("Descodifica: "))
    print(descodifica(n))
