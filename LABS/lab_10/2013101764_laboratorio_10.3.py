# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 10.3
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

        
class Enfermedad:
    def __init__(self,pn="",ps="",pt=""):
        self.nombre = pn
        self.sintomas = ps
        self.tratamiento = pt

    def setNombre(self, var):
        self.nombre = var
    def getNombre(self):
        return self.nombre

    def __str__ (self):
        return "\n\tEnfermedad: "+self.nombre+"\n\t\tSintomas: "+self.sintomas+"\n\t\tTratamiento: "+self.tratamiento

    def __lt__(self,pe):
        return self.nombre < pe.nombre

class Paciente:
    def __init__(self,pn="",pe="",pg=""):
        self.nombre = pn
        self.edad = pe
        self.genero = pg
        self.enfermedades = []

    def addEnfermedad(self,var):
        self.enfermedades.append(var)

    def setNombre(self, var):
        self.nombre = var
    def getNombre(self):
        return self.nombre

    def __str__ (self):
        res = "Nombre: "+self.nombre+"\n\tEdad: "+self.edad+"\n\tGenero: "+self.genero
        for i in self.enfermedades:
            res += str(i)
        return res

    def __lt__(self,pe):
        return self.nombre < pe.nombre
    
    

    

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

listaP = []
##enfermedades automaticas
buffer = Paciente("Ema","26","M")
bufferE = Enfermedad("Calambre","Dolor intenso","Voltaren")
buffer.addEnfermedad(bufferE)
listaP.append(buffer)

buffer = Paciente("Ana","25","F")
bufferE = Enfermedad("ansiedad","inestabilidad emocional","vacaciones")
buffer.addEnfermedad(bufferE)
listaP.append(buffer)

buffer = Paciente("Vale","27","F")
bufferE = Enfermedad("Varicela","Fiebre y ronchas","Descanso y fiesta de varicela")
buffer.addEnfermedad(bufferE)
listaP.append(buffer)

buffer = Paciente("Yaja","25","F")
bufferE = Enfermedad("Calambre","Dolor intenso","Voltaren")
buffer.addEnfermedad(bufferE)
listaP.append(buffer)

buffer = Paciente("Ale","28","M")
bufferE = Enfermedad("Caspa","piel muerta en cabello","manteca de coco")
buffer.addEnfermedad(bufferE)
listaP.append(buffer)

listaP.sort()

##menu para agragar nuevas enfermedades

n = ""
while (n != "q"):
    n = input("Presione a para agregar paciente, p para imprimir lista o q para salir: ")
    if (n == "a"):
        a = input("Nombre: ")
        b = input("Edad: ")
        c = input("Genero: ")
        buffer = Paciente(a,b,c)
        j = ""
        while (j != "q"):
            j = input("Presione e para agregar enfermedad o q para continuar: ")
            if (j == "e"):
                d = input("Enfermedad: ")
                e = input("sintomas: ")
                f = input("Tratamiento: ")
                buffer.addEnfermedad(Enfermedad(d,e,f))
        listaP.append(buffer)
        listaP.sort()
    elif(n == "p"):
        for e in listaP:
            print(e)



