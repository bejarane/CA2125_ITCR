# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 3.3.2
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

##finalizar cono, cilindro y piramide con area y volumen


##ejemplo
def convertidor(h,m,s):
    return h * 3600 + m * 60 +s

#programa
h1 = int(input("Indique las horas del primer tiempo:"))
m1 = int(input("Indique los minutos del primer tiempo:"))
s1 = int(input("Indique los segundos del primer tiempo:"))
print()
h2 = int(input("Indique las horas del segundo tiempo:"))
m2 = int(input("Indique los minutos del segundo tiempo:"))
s2 = int(input("Indique los segundos del segundo tiempo:"))
print()
print("La diferencia es:", abs(convertidor(h2,m2,s2) - convertidor(h1,m1,s1)), "s")

