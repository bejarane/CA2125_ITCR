# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 3.5
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

def costo_Horas(h):
    total = 0;

    if h < 24:
        if h < 20:
            if h < 3:
                total = 500
            else:
                total = 500 + (h-3)*150*2
        else:
            total = 5700
    else:
        ##maximo de horas
        print("exceso de horas")
    return total

def costo_Total(c_H, n_A):
    return  c_H * n_A
    


#programa
print("Calculo potencia:")
horas = float(input("Indique las hora:"))
autos = float(input("Indique los autos:"))
c_A = costo_Horas(horas)
c_T = costo_Total(c_A,autos)
print("El costo por auto es:", c_A, " y el total es:", c_T)
