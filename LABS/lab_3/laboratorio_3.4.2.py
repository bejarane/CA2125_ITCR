# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 3.4.2
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

def corriente_R (voltaje,ohm):
    return voltaje/ohm ##viene de la ecuacion V= I*R

def potencia_R (voltaje, ohm): ##calcula la potencia de un componente conocimiendo el voltaje y su resistencia
    return voltaje * corriente_R(voltaje,ohm) ##la ecuacion de potencia es P = V* I


##calcula la perdida de presion para una tuberia de pvc que transporta agua
## a temperatura ambiente. los parametros de entrada son caudal l/s, longitud de
##tuberia en metros y diamtero interno de tuberia en mm
## la ecuacion original es  hf = 10.678 * L  * (Q) ** 1.852
##                                 D**4.87     (C)
## siendo l metros, q m3/h, d metros y c una constante de 150 para PVC

def caudal_M3 (caudal):
    return caudal / 1000 ##cambia de l/s a m3/s

def perdida_F (caudal, longitud, diametro):
    return longitud * (3.5881 * caudal_M3(caudal)/150/(diametro/1000)**2.63)**1.8518


#programa
print("Calculo potencia:")
vol = float(input("Indique el voltaje:"))
res = float(input("Indique la resistencia:"))
print("La potencia es:", potencia_R(vol,res), "W")

print()
print("Calculo perdida de presion:")
q = float(input("Indique el caudal (l/s):"))
l = float(input("Indique la longitud (m):"))
d = float(input("Indique el diametro interno (mm):"))
print("La perdida es:", round(perdida_F(q,l,d),4),"MCA")

