# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 6.2
#
#   FECHA: 21/05/20
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

lista = []
cuantas = int(input("Cuantas notas va a digitar: "))

while len(lista) < cuantas:
    nota = int(input("Digite la nota (entre o y 9): "))
    if nota >= 0 and nota <= 9:
        lista.append(nota)
    else:
        print("Nota fuera de rango, digite de nuevo.")

contadores = [0,0,0,0,0,0,0,0,0,0]

for x in lista:
    contadores[x] += 1

maximo_conteo = max(contadores)
indice = contadores.index(maximo_conteo)

for y in range(maximo_conteo,0,-1):
    linea = str(y)
    for x in range(0,10):
        if contadores[x] >= y:
            linea += " *"
        else:
            linea += "  "
    print(linea)
print("  0 1 2 3 4 5 6 7 8 9")

