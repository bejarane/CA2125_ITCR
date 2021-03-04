# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Examen pregunta 2
#
#   FECHA: 28/05/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
#
###########################################################

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] ##lista predictada


####tambien puede ser pedida por terminal
##n = eval(input("Cantidad de numeros a igresar: "))
##numeros = []
##for i in range(n):
##    num = eval(input("Numero %d: " % (i+1)))
##    numeros.append(num)

longitud = len(numeros)
if longitud > 10:
    longitud = 10 ##fija tamaño en caso de ser mas de 10

suma = 0
for i in range(longitud):
    suma += numeros[i]

print("La lista es: ")
print(numeros)
print("La suma es: ")
print(suma)
