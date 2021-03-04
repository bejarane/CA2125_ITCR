# coding=utf-8
#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 1.4
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


#masa = presion x volumen / (0.37*temperatura+460)


p = float(input("Indique la presion: ")) ##la lectura que toma la convierte a numero de punto flotante
v = float(input("Indique el volumen: "))
t = float(input("Indique la temperatura: "))

m = p * v / (0.37 * (t+460))

print("La masa es: ",m)
