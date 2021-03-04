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

entradaA = ["hhoola","hhoolaaa","hola ola", "holala", "una larga cadena que solo contiene un hola al final"]
busqueda = "hola"
for entrada in entradaA:
    print("Cadena: %s" % entrada)

    print("Metodo por loop en lista de indices")

    #entrada = input("Ingrese la frase a analizar: ")

    ##se remueven los caracteres que no interesan para reducir iteraciones
    entrada = entrada.lower() ##todo minusculas
    entradaL = ""
    letraH = []
    letraO = []
    letraL = []
    letraA = []

    pasos = 0 ##un contador de iteraciones

    for i in range(len(entrada)):
        pasos += 1
        if entrada[i] == 'h':
            letraH.append(i)
        if entrada[i] == 'o':
            letraO.append(i)
        if entrada[i] == 'l':
            letraL.append(i)
        if entrada[i] == 'a':
            letraA.append(i)
            

    ##con un string sin caracteres innecesarios
    pO = 0
    pL = 0
    pA = 0
    for h in letraH:
        pasos += 1
        for o in letraO:
            pasos += 1
            pO += 1
            break
            if h < o:
                pO += 1
                for l in letraL:
                    pasos += 1
                    if o < l:
                        pL += 1
                        for a in letraA:
                            pasos += 1
                            if l < a:
                                pA += 1

    print("\tLe resultado es: %d, %d, %d" % (pO,pL,pA))
    print("\tIteraciones necesarias: %d" % (pasos))

    print("Metodo por loop directo en cadena de texto")
    #entrada = input("Ingrese la frase a analizar: ")

    ##se remueven los caracteres que no interesan para reducir iteraciones
    entrada = entrada.lower() ##todo minusculas
    entradaL = ""

    pasos = 0
    for i in entrada:
        pasos += 1
        if i in busqueda:
            entradaL += i

    ##con un string sin caracteres innecesarios
    longitud = len(entradaL)
    conteo = 0
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

    print("\tLa cadena %s se combina %d veces" %(busqueda,conteo))
    print("\tIteraciones necesarias: %d" % (pasos))
    print()
