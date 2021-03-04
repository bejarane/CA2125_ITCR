# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 3.2
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

def cualitativa(nota_E):
    if nota_E < 5.0:
        return "Reprobado"
    elif nota_E >= 5.0 and nota_E < 7.0:
        return "Suspenso"
    elif nota_E >= 7.0 and nota_E < 8.5:
        return "Notable"
    elif nota_E >= 8.5 and nota_E < 10.0:
        return "Sobresaliente"
    elif nota_E == 10:
        return "Matricula de honor"
    return ""


print("La nota es:",cualitativa(float(input("Ingrese la nota: "))))


##solucion profesor
def Calificacion(n):
    palabra = ""
    if n < 5.0:
        palabra = "Reprobado"
    elif n >=5.0 and n < 7.0:
        palabra = "Suspenso"
    elif n >= 7.0 and n <= 8.5:
        palabra = "Notable"
    elif n >= 8.5 and n < 10.0:
        palabra = "Sobresaliente"
    elif n == 10:
        palabra = "Matricula de honor"

    return palabra


