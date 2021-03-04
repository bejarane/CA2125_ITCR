# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 2.10
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
#//////////////////Fucion Principal///////////////////////#
###########################################################


try:
    m2_T = int(input("Digite el numero de hectareas: "))*10000 ##conversion a m2

    if m2_T <= 1000000:
        pino_M2 = 0.5 * m2_T
        eucalipto_M2 = 0.3 * m2_T
        cedro_M2 = 0.3 * m2_T
    else:
        pino_M2 = 0.7 * m2_T
        eucalipto_M2 = 0.2 * m2_T
        cedro_M2 = 0.1 * m2_T

    pino_N = int(pino_M2/10*8)
    eucalipto_N = int(eucalipto_M2) ## No convierte porque x/15 *15 = x
    cedro_N = int(cedro_M2/18*10)


  

    print("En el area se deben sembrar: ",pino_N, " pinos, ",eucalipto_N," eucaliptos y ", cedro_N, " cedros.")


except ValueError:
    print("Error de entrada. Valor no reconocido: ValueError")
    
   
