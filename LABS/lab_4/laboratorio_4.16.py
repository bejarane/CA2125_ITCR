# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 4.16
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

##hacer tarea de los pares restantes

n= int(input("Digite la cantidad de alumnos:"))
##m = int(input("Digite el final del rango:"))

suma = 0
text = "nota del alumno "

for g in range(1,n+1):
    
    suma = suma + eval(input(text + str(g) + ": "))
    
print("El promedio de las calificaciones es:", suma/n)     

