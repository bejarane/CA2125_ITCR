# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 6.6
#
#   FECHA: 26/05/20
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

cantidad = int(input("Digite cuantas palabras quiere (1-10): "))

while cantidad <= 0 or cantidad > 10:
    print("La cantidad tiene que estar entre 1 y 10. Intende de nuevo")
    cantidad = int(input("Digite cuantas palabras quiere (1-10): "))

lista = []
while len(lista) < cantidad:
    palabra = input("Digite una palabra: ")
    if palabra not in lista:
        lista.append(palabra)
    else:
        print ("La palabra esta repetida")

#fin del ciclo
print ("Lista de palabras: ")
print (lista)

cantidad_frases = int(input("Digite cuantas frases quiere (1-5): "))
while cantidad <= 0 or cantidad > 10:
    print("La cantidad tiene que estar entre 1 y 10. Intende de nuevo")
    cantidad_frases = int(input("Digite cuantas frases quiere (1-5): "))

frases = []
while len(frases) < cantidad_frases:
    f = input("Digite la frase: ")
    frases.append(f)

print("Lista de frases")
print(frases)

for p in lista:
    contar  = 0
    for f in frases:
        contar += f.count(p)

    print("palabra: %s aparece: %d" % (p,contar))

