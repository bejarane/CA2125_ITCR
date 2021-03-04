# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 11.4
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
    
class Cuadrilatero:
    def __init__(self,p1=[0,0],p2=[0,1],p3=[1,1],p4=[1,0]):
        self.punto1 = p1
        self.punto2 = p2
        self.punto3 = p3
        self.punto4 = p4
    
    def Imprimir(self):
        print("Punto 1:",self.punto1)
        print("Punto 2:",self.punto2)
        print("Punto 3:",self.punto3)
        print("Punto 4:",self.punto4)

class Trapezoide(Cuadrilatero):
    def __init__(self,p1=[0,0],p2=[0,1],p3=[1,1],p4=[1,0]):
        super().__init__(p1,p2,p3,p4)
    def Imprimir(self):
        super().Imprimir()
    
class Paralelogramo(Cuadrilatero):
    def __init__(self,p1=[0,0],p2=[0,1],p3=[1,1],p4=[1,0]):
        super().__init__(p1,p2,p3,p4)
    def Imprimir(self):
        super().Imprimir()

class Rectangulo(Paralelogramo):
    def __init__(self,p1=[0,0],p2=[0,1],p3=[1,1],p4=[1,0]):
        super().__init__(p1,p2,p3,p4)
    def Imprimir(self):
        super().Imprimir()

class Cuadrado(Rectangulo):
    def __init__(self,p1=[0,0],p2=[0,1],p3=[1,1],p4=[1,0]):
        super().__init__(p1,p2,p3,p4)
    def Imprimir(self):
        super().Imprimir()


###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

print("Cuadrilatero")
c1= Cuadrilatero([1,1],[2,2],[3,3],[4,4])
c1.Imprimir()
print()

print("Trapezoide:")
t1= Trapezoide([7,7],[6,6],[8,8],[9,9])
t1.Imprimir()
print()

print("Paralelogramo:")
p1=Paralelogramo([1,2],[2,3],[3,4],[4,5])
p1.Imprimir()
print()

print("Rectangulo:")
r1=Rectangulo([10,10],[11,11],[12,12],[13,13])
r1.Imprimir()
print()

print("Cuadrado:")
cd1=Cuadrado([1,3],[2,4],[3,5],[4,6])
cd1.Imprimir()
print()