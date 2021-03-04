# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 10.4
#
#   FECHA: 25/06/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
###########################################################

###########################################################
#//////////////////Clases/////////////////////////////////#
###########################################################

class Mistring:
    def __init__(self,ps=""):
        self.s = ps

    def __str__(self):
        return self.s

    def find(self,busco,inicio=0,fin=0,lista=[]):
        if len(lista)==0: ##si no hay lista, evaluar self
            if (fin==0): ##si fin no definido, definir
                fin = len(self.s)-1 ##-1 para que fin inicie en 0
            elif (fin > len(self.s)-1): ##si fin es mayor que array
                fin = len(self.s)-1
            for i in range(inicio,fin+1): ##recorrer array
                if (self.s[i] == busco):
                    return i
            return -1
        else:
            if (fin==0):
                fin = len(lista)-1
            elif (fin > len(lista)-1):
                fin = len(lista)-1
            for i in range(inicio,fin+1):
                if (busco in lista[i]):
                    return i
            return -1

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################
ms1 = Mistring("hola mundo")

print(ms1.find("o",5,7)) ##posiciones contando desde 0

print(ms1.find("o",0,1,["gris", "morado","azul"]))


