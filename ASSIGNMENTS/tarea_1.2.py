# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Tarea 1.2
#
#   FECHA: 08/06/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
#
###########################################################

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################


#restricciones:
##“matriz” que tiene los datos.
matriz = []
##“n” que tiene la cantidad de filas y columnas de “matriz”
n=5 #columnas de matriz




m=n #filas de matriz igual a n (los ejemplos de figura en la tarea eran de 5x8, donde n!=m)

lista = ['a','b','c','d','e','f','g','h','i','j','k','l']

for i in range(0,m):
    fila = []
    for j in range(0,n):
        fila.append(lista[j]+str(i))
    matriz.append(fila)

###metodo manual
##matriz = []
##n = int(input("Indique tamaño matriz: "))
##for r in range(n):
##    matriz.append([0]*n)
##
##for r in range(n):
##    for t in range(n):
##        matriz[r][t] = int(input("Ingrese valor %d, %d: " % (r,t)))


print("La matriz es: ")
for f in matriz:
    print(f)

##proceso imprimir en forma E:
##Imprimir toda la primera y  ultima fila
##Imprimir siempre la primera casilla
##Si m es par, imprimir la fila del centro arriba,
##si m es impar, imprimir la fila del centro
##imprimir toda la ultima fila
print("Imprimiendo los valores con el patron E")

lenM = len(matriz)
ultimaF = lenM - 1
lenF = len(matriz[0])
centroF = lenM//2
if (lenM%2 == 0):
    centroF -= 1

for i in range(lenM):
    if i == 0 or i == ultimaF:
        for j in matriz[i]:
            print (j)
    elif i == centroF:
        for j in range(lenF-1):
            print(matriz[i][j])
    else:
        print (matriz[i][0])
    

    

