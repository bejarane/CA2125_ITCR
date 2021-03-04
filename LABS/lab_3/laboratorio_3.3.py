# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 3.3
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
import math

def a_b_Cono(r):
    return (math.pi * r ** 2)

def a_l_Cono(r,G):
    return math.pi * r * G

def a_Total (ab, al):
    return ab + al

def v_Cono (ab,h):
    return ab*h/3

def h_Cono (r,g):
    return math.sqrt(g**2-r**2)

def ab_Cilindro (r):
    return math.pi*r**2

def al_Cilindro (r,h):
    return 2*math.pi*r*h

def at_Cilindro (r,h):
    return 2*ab_Cilindro(r) + al_Cilindro(r,h)

def vol_Cilindro (r,h):
    return ab_Cilindro(r)*h

#programa
print("Area y volumen del cono:")
print("--------------")
r = float(input("Indique el radio:"))
g = float(input("Indique la generatriz:"))
print("Area es:", a_Total( a_b_Cono(r) , a_l_Cono(r,g) ))
print("Volumen es:", v_Cono(a_b_Cono(r),h_Cono(r,g)))

print()

print("Area y volumen de la piramide:")
print("--------------")
bP = float(input("Indique area de base:"))
lP = float(input("Indique area de lado:"))
h = float(input("Indique altura:"))
print("Area es:", a_Total( bP , lP ))
print("Volumen es:",v_Cono(bP,h))

print()

print("Area y volumen del cilindro:")
print("-------------")
cR = float(input("Indique el radio:"))
cH = float(input("Indique la altura:"))
print("Area es:", at_Cilindro(cR,cH))
print("Volumen es:", vol_Cilindro(cR,cH))

