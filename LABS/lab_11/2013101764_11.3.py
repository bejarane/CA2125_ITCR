# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 11.3
#
#   FECHA: 02/07/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
###########################################################

###########################################################
#//////////////////Clases/////////////////////////////////#
###########################################################  

class Cambio:
    def __init__(self,pp=0):
        self.piñones = pp

    def Imprimir(self):
        print("Cambios dispnibles: ",self.piñones)


class Aro:
    def __init__(self,tm=0,tp=""):
        self.tamano = tm
        self.tipo = tp
    
    def Imprimir(self):
        print("Tamaño de aro: ",self.tamano)
        print("Tipo: ",self.tipo)

class Marco:
    def __init__(self,pm="",pt=""):
        self.material = pm
        self.tipo = pt
        
    def Imprimir(self):
        print("Material del marco:",self.material)
        print("Marco para: ",self.tipo)
    
class Bicicleta(Cambio,Aro,Marco):
    def __init__(self, pp=0,tm=0,tp="",pm="",pt=""):
        Cambio.__init__(self,pp)
        Aro.__init__(self,tm,tp)
        Marco.__init__(self,pm,pt)
        
    def Imprimir(self):
        Cambio.Imprimir(self)
        Aro.Imprimir(self)
        Marco.Imprimir(self)

    
###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################   
    
b1 = Bicicleta(5,24,"ruta","Aluminio","Ruta")
b1.Imprimir()
print()

b2 = Bicicleta(21,29,"MBX","Titanio","Montaña")
b2.Imprimir()
