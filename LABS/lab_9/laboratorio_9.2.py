# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 9.2
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

class Tiempo:
    horas = 0
    minutos = 0
    segundos = 0

    def SetHora(self,value):
        self.horas = value
    def GetHora(self):
        return self.horas

    def SetMinuto(self, value):
        self.minutos = value
    def GetMinuto(self):
        return self.minutos

    def SetSegundo(self,value):
        self.segundos = value
    def GetSegundo(self):
        return self.segundos

    def Imprimir(self):
        print("Hora: %d, minuto: %d, segundos: %d" % (self.horas,self.minutos,self.segundos))

    def Diferencia(self, t2):
        hh = abs(self.horas - t2.horas)
        mm = abs(self.minutos - t2.minutos)
        ss = abs(self.segundos - t2.segundos)
        return '''Diferencia:
    Hora: %d, minuto: %d, segundos: %d''' % (hh,mm,ss)
        



#programa
t1 = Tiempo()
t1.SetHora(7)
t1.SetMinuto(50)
t1.SetSegundo(2)
t1.Imprimir()

t2 = Tiempo()
t2.SetHora(8)
t2.SetMinuto(51)
t2.SetSegundo(0)
t2.Imprimir()

print(t1.Diferencia(t2))
print(t2.Diferencia(t1))
    

