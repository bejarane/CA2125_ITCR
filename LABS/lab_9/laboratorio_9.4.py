# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 9.4
#
#   FECHA: 11/06/20
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
#clases / concepto
import math

class Cubo:
    lado = 2
    
    def SetLado(self,pl):
        self.lardo = pl
    def GetLado(self):
        return self.lardo
    
    def GetVolumen(self):
        return self.lado ** 3

class Cilindro:
    radio = 1
    alto = 2

    def SetRadio(self,value):
        self.radio = value
    def GetRadio(self):
        return self.radio

    def SetAlto(self,value):
        self.alto = value
    def GetAlto(self):
        return self.alto

    def AreaBase (self):
        return math.pi * self.radio ** 2

    def GetVolumen (self):
        return self.AreaBase() * self.alto

##class Cono:
##    ##creo que a esto se refiere con "reutilice clases donde se posean subfiguras geometricas iguales"
##    cilindro = Cilindro()
##
##    def SetRadio(self,value):
##        self.cilindro.SetRadio(value)
##    def GetRadio(self):
##        return self.cilindro.GetRadio()
##
##    def SetAlto(self,value):
##        self.cilindro.SetAlto(value)
##    def GetAlto(self):
##        return self.cilindro.GetAlto()
##
##    def GetVolumen (self):
##        return self.cilindro.GetVolumen() / 3 ##volumen del cono es igual al cilindro, pero entre 3
    
class Cono:
    radio = 1
    alto = 2

    def SetRadio(self,value):
        self.radio = value
    def GetRadio(self):
        return self.radio

    def SetAlto(self,value):
        self.alto = value
    def GetAlto(self):
        return self.alto

    def AreaBase (self):
        return math.pi * self.radio ** 2

    def GetVolumen (self):
        return self.AreaBase() * self.alto / 3



#programa
c1 = Cubo()
c1.SetLado(4)

print("Volumen Cubo :", c1.GetVolumen())

c2 = Cilindro()
c2.SetRadio(5)
c2.SetAlto(10)

print("Volumen Cilindro: ", c2.GetVolumen())

c3 = Cono()
c3.SetRadio(5)
c3.SetAlto(10)

print("Volumen Cono: ", c3.GetVolumen())





