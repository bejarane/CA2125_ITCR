# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 13.2
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

diccionario = {}

cuantas = int(input("Cuantas palabras: "))
for i in range(cuantas):
    spa = input("Palabra en español: ")
    eng = input("Traducción al inglés: ")
    diccionario[spa] = eng

print(diccionario)

#traducir
palabra =input("Palabra a traducir: ")
if palabra in diccionario.keys():
    print("La traducción es: ", diccionario[palabra])
else:
    print("La palabra no esta en el diccionario.")

#eliminar
palabra  = input("Palabra a eliminar: ")
if palabra in diccionario.keys():
    del diccionario[palabra]
    print("Palabra borrada.")
else:
    print("La palabra no esta en el diccionario")

#cambiar
palabra =input("Palabra a cambiar traduccion: ")
if palabra in diccionario.keys():
    nueva = input("Nueva traducción: ")
    diccionario[palabra]=nueva
else:
    print("La palabra no esta en el diccionario.")

#lista de palabras
print("Palabras en español: ")
print(diccionario.keys())

print("Palabras en otro idioma: ")
print(diccionario.values())
