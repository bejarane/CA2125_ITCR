# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 9.3
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

class Rectangulo:
    largo = 1
    ancho = 1
    

    def SetLargo(self,pl):
        if pl>=0 and pl <= 20.0:
            self.largo = pl
        else:
            print("Valor fuera del rango.")
    def GetLargo(self):
        return self.largo
    

    def SetAncho(self,pa):
        if pa>=0 and pa <= 20.0:
            self.ancho = pa
        else:
            print("Valor fuera del rango.")
    def GetAncho(self):
        return self.ancho
    

    def Area(self):
        return self.ancho * self.largo

    def Perimetro(self):
        return 2*(self.ancho + self.largo)

    def EsCuadrado(self):
        return (self.ancho - self.largo) <= 0.0001 ##toma en cuenta cualquier error por numeros flotantes


#programa
r1 = Rectangulo()
r1.SetAncho(20)
r1.SetLargo(20)

print("Perimetro :", r1.Perimetro())
print("Area :", r1.Area())
print("Es cuadrado :", r1.EsCuadrado())

