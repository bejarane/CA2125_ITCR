# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Examen pregunta 5
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


##se hace un doble for donde va avanzando de letra en letra y
##estimando si hay las letras necesarias por detrás y delante
##inmediato

entrada = "holala"
busqueda = "hola"

##se remueven los caracteres que no interesan para reducir iteraciones
entrada = entrada.lower() ##todo minusculas
entradaL = ""
for i in entrada:
    if i in busqueda:
        entradaL += i

##con un string sin caracteres innecesarios
longitud = len(entradaL)
conteo = 0
pasos = 0
for i in range(longitud):
    ##print("",entradaL[i])
    pasos += 1
    if entradaL[i] == "h":
        for j in range(i+1,longitud): ##i+1 para no revisar de nuevo
            pasos += 1
            ##print("\t",entradaL[j])
            if entradaL[j] == "o":
                for k in range(j+1,longitud):
                    pasos += 1
                    ##print("\t\t",entradaL[k])
                    if entradaL[k] == "l":
                        for l in range(k+1, longitud):
                            pasos += 1
                            ##print("\t\t\t",entradaL[l])
                            if entradaL[l] == "a":
                                conteo = conteo + 1

print(conteo)
print(pasos)


##metodo mas eficiente que reduce la cantidad de loops y permite el cambio
##dinamico de el string de busqueda
long1 = len(entrada)
long2 = len(busqueda)

contador = [0]*(long2+1) ##dejar un campo extra para una restriccion del algoritmo
virtual = [0]*(long2+1)
virtualPar = [0]*(long2+1)

pasos = 0

print("\nmetodo 2")

for i in range(long1): ##no usa el strip para evitar un pase
    pasos += 1
    if entrada[long1-1-i] in busqueda:
        for j in range(long2): ##no necesita evaluar al primero
            pasos += 1
            #print(i)
            if entrada[long1-1-i] == busqueda[long2-1-j]:
                virtual[long2-1-j] += 1
                virtualPar[long2-j] += 1
                contador[long2-j] += virtual[long2-j]
                virtual[long2-j] = 0
                ##print("found",entrada[long1-1-i])
                break
    
    print("contador: %d, virtual: %d" % (contador[0],virtual[0]))
    print("contador: %d, virtual: %d" % (contador[1],virtual[1]))
    print("contador: %d, virtual: %d" % (contador[2],virtual[2]))
    print("contador: %d, virtual: %d" % (contador[3],virtual[3]))
    print(entrada[long1-1-i])
    print("---------------")

total = virtual[0]
for i in contador:
    if i > 0:
        total = total * i

print(total)
print(pasos)
        
