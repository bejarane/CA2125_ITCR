# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 10.1
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
#se definen tres clases paciente, enfermedad y tratamiento
#cada paciente tiene una lista de enfermedades
#cada enfermedad tiene una lista de tratamientos

class Tratamiento:
    def __init__(self):
        self.tipo = input("Tipo de tratamiento: ")
        self.descripcion = input("Descripcion: ")
        self.dosis = input("Dosis: ")
    def setTipo(self,var):
        self.tipo = var
    def getTipo(self):
        return self.tipo
    def setDesc(self,var):
        self.descripcion = var
    def getDesc(self):
        return self.descripcion
    def setDosis(self,var):
        self.dosis = var
    def getDosis(self):
        return self.dosis
    def print(self):
        print("\t\tTipo de tratamiento:",self.tipo)
        print("\t\tDescripción:",self.descripcion)
        print("\t\tDosis:",self.dosis)
        print("")

    
        
class Enfermedad:
    def __init__(self):
        self.nombre = input("Nombre enfermedad: ")
        self.causa = input("Causa enfermedad: ")
        self.tratamientos = []
        n = int(input("Cantidad de tratamientos: "))
        for i in range(n):
            self.addTratamiento()
    def setNombre(self, var):
        self.nombre = var
    def getNombre(self):
        return self.nombre
    def setCausa(self,var):
        self.causa = var
    def getCausa(self):
        return self.causa
    def addTratamiento(self):
        buffer = Tratamiento()
        self.tratamientos.append(buffer)
    def getTratamiento(self):
        return self.tratamientos
    def print (self):
        print("\tEnfermedad:",self.nombre)
        print("\tCausa:",self.causa)
        print("\tTratamientos:")
        for i in self.tratamientos:
            i.print()
        print("")
    

class Paciente:
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.genero = input("Genero: ")
        self.edad = input("Edad: ")
        self.peso = input("Peso: ")
        self.estatura = input("Estatura: ")
        self.enfermedades = []
        n = int(input("Cantidad de enfermedades: "))
        for i in range(n):
            self.addEnfermedad()
        
    def setNombre(self, var):
        self.nombre = var
    def getNombre(self):
        return self.nombre
    def setGenero(self,var):
        self.genero = var
    def getGenero(self):
        return self.genero
    def setEdad (self, var):
        self.edad = var
    def getEdad (self):
        return self.edad
    def setEstatura (self, var):
        self.estatura = var
    def getEstatura (self):
        return self.estatura
    def addEnfermedad(self):
        buffer = Enfermedad()
        self.enfermedades.append(buffer)
    def print (self):
        print("Nombre del paciente:",self.nombre)
        print("Genero:",self.genero)
        print("Edad:",self.edad)
        print("Peso:",self.peso)
        print("Estatura:",self.estatura)
        print("Enfermedades:")
        for i in self.enfermedades:
            i.print()
    

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

paciente1 = Paciente()
print("\n")

paciente1.print()

