# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 8.1
#
#   FECHA: 14/07/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
########################################################### 

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

lista = []
cuantos = int(input("Indique cuantos nombres quiere: "))
for i in range(1,cuantos+1):
    nombre = input("Nombre: ")
    t = (i,nombre)
    lista.append(t)

print (lista)

numero =  int(input("Numero a buscar: "))
encontro = False

for t in lista:
    if numero == t[0]:
        print("Si existe.")
        print("Nombre:",t[1])
        encontro = True
        break
if encontro == False:
    print("No se encuentra el numero indicado")
