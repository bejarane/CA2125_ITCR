# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 6.12
#
#   FECHA: 28/05/20
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

def binaria (array, key):
    pMax = len(array)-1
    pMin = 0
    ##puntero = (pMax - pMin)//2
    while pMax != pMin and key <= array[pMax] and key >= array[pMin]:
        puntero = (pMax - pMin)//2
        ##print("en while")
        valor = array[puntero]
        if valor > key:
            pMax = puntero - 1
        elif valor < key:
            pMin = puntero + 1
        else:
            return puntero

    if array[pMax] == key:
        return pMax
    elif array[pMin] == key:
        return pMin
    else:
        return -1

def interpolada (array, key):
    pMax  = len(array)-1
    pMin = 0
    
    while pMax != pMin and key <= array[pMax] and key >= array[pMin]:
        puntero = pMin + int((key - array[pMin]) * (pMax - pMin)/(array[pMax]- array[pMin]))
        ##print("puntero",puntero)
        valor = array[puntero]
        if valor < key:
            pMin = puntero + 1
        if valor > key:
            pMax = puntero -1
        else:
            return puntero
    if array[puntero] == key:
        return puntero
    else:
        return -1

n = eval(input("Tamaño de la lista: "))


lNombre = []
lIndex = []

contador = 1
for i in range(n):
    nombre = (input("Ingrese el nombre %d: " % (contador)))
    lNombre.append(nombre)
    lIndex.append(contador)
    contador += 1

print(lNombre)
print(lIndex)
    
x = eval(input("Ingrese una posición a buscar: "))

print("Por busqueda binaria")
posi = binaria(lIndex,x)
if posi >= 0:
    print("Valor encontrado %s" %(lNombre[posi]))
else:
    print("Valor no encontrado")

print("\n")
print("Por busqueda interpolada")
posi = interpolada(lIndex,x)
if posi >= 0:
    print("Valor encontrado %s" %(lNombre[posi]))
else:
    print("Valor no encontrado")
