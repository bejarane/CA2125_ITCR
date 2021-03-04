# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 5.16
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
p1 = input("Digite la palabra 1: ")
p2 = input("Digite la palabra 2: ")
p3 = input("Digite la palabra 3: ")
p4 = input("Digite la palabra 4: ")
p5 = input("Digite la palabra 5: ")

menor = p1

if p2[0] < menor[0]:
    menor = p2

if p3[0] < menor[0]:
    menor = p3

if p4[0] < menor[0]:
    menor = p4

if p5[0] < menor[0]:
    menor = p5

print("La palabra menor es: ", menor)
