# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 11.2
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

class Empleado:
    def __init__ (self,pn="",pa="",pt="",pd="",ps=""):
        self.nombre = pn
        self.apellido=pa
        self.telefono=pt
        self.direccion=pd
        self.seguro=ps
    
    def Imprimir(self):
        print("Nombre: ",self.nombre)
        print("Apellidos: ",self.apellido)
        print("Telefono: ",self.telefono)
        print("Direccion: ",self.direccion)
        print("seguro: ",self.seguro)

class ESalario(Empleado):
    def __init__(self,pn="",pa="",pt="",pd="",ps="",ss=0):
        super().__init__(pn,pa,pt,pd,ps)
        self.salario = ss

    def Imprimir(self):
        super().Imprimir()
        print("Salario/semana: ",self.salario)


class EHora(Empleado):
    def __init__(self,pn="",pa="",pt="",pd="",ps="",sh=0,nh=0):
        super().__init__(pn,pa,pt,pd,ps)
        self.salario = sh
        self.horas = nh
    
    def Imprimir(self):
        super().Imprimir()
        print("Salario/hora: ",self.salario)
        print("Horas: ", self.horas)
        


class EComision(Empleado):
    def __init__(self,pn="",pa="",pt="",pd="",ps="",pc=0,dv=0):
        super().__init__(pn,pa,pt,pd,ps)
        self.porcentaje = pc
        self.ventas = dv
    
    def Imprimir(self):
        super().Imprimir()
        print("Comisión: ", self.porcentaje,"%")
        print("Ventas: ",self.ventas)


###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

e = ESalario("Jule", "Viole Grace", "25","Torre","25BAM",5000)
e.Imprimir()
print()

e1 = EHora("Marta","Valerio Viquez","8885-7","Cartago","1-234-567",8000,12,)
e1.Imprimir()
print()

e2 = EComision("Manuel","Vega Rojas", "8899556677","Lejos","A-55582R",12,5000)
e2.Imprimir()