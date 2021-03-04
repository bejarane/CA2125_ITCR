# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 9.1
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

class Mesa:
    forma = "cuadrada"
    capacidad = 10

    def setForma(self,value):
        self.forma = value

    def getForma(self):
        return self.forma


    def setCapacidad(self,value):
        self.capacidad = value

    def getCapacidad(self):
        return self.capacidad

class Persona:
    estatura = 1.60
    género = "indefinido"

    def setEstatura(self,value):
        self.estatura = value

    def getEstatura(self):
        return self.estatura


    def setGenero(self,value):
        self.genero = value

    def getGenero(self):
        return self.genero

class Revista:
    año = 2012
    temática = "gossip"

    def setAño(self,value):
        self.año = value

    def getAño(self):
        return self.año


    def setTematica(self,value):
        self.tematica = value

    def getTematica(self):
        return self.tematica

class Camisa:
    color = "Azul"
    talla = "XL"

    def setColor(self,value):
        self.color = value

    def getColor(self):
        return self.color


    def setTalla(self,value):
        self.talla = value

    def getTalla(self):
        return self.talla



#programa
unamesa = Mesa()
unamesa.setForma("Redonda")
print(unamesa.getForma())

unapersona = Persona()
unapersona.setEstatura(1.5)
print(unapersona.getEstatura())

unarevista = Revista()
unarevista.setAño(2200)
print(unarevista.getAño())

unacamisa = Camisa()
unacamisa.setTalla("M")
print(unacamisa.getTalla())

