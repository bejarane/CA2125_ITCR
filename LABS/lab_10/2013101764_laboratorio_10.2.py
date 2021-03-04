# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 10.2
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
        return "Nombre: "+self.nombre+"\n\tSintomas: "+self.sintomas+"\n\tTratamiento: "+self.tratamiento

    def __lt__(self,pe):
        return self.nombre < pe.nombre
    

    

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

listaE = []
##enfermedades automaticas
buffer = Enfermedad("z_covid-19","Fiebre y dolor","aislamiento")
listaE.append(buffer)
buffer = Enfermedad("Varicela","Fiebre y ronchas","Descanso y fiesta de varicela")
listaE.append(buffer)
buffer = Enfermedad("Calambre","Dolor intenso","Voltaren")
listaE.append(buffer)
buffer = Enfermedad("ansiedad","inestabilidad emocional","vacaciones")
listaE.append(buffer)
buffer = Enfermedad("Caspa","piel muerta en cabello","manteca de coco")
listaE.append(buffer)
listaE.sort()


##menu para agragar nuevas enfermedades

n = ""
while (n != "q"):
    n = input("Presione a para agregar enfermedad, p para imprimir lista o q para salir: ")
    if (n == "a"):
        a = input("Nombre de enfermedad: ")
        b = input("sintomas enfermedad: ")
        c = input("Tratamiento de la enfermedad: ")
        listaE.append(Enfermedad(a,b,c))
        listaE.sort()
    elif(n == "p"):
        for e in listaE:
            print(e)



