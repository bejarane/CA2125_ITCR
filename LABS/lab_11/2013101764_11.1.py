# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 11.1
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

class MiembroComunidad:
    def __init__(self,pn=""):
        self.nombre = pn

    def Imprimir(self):
        print("Nombre :",self.nombre)
    

class Empleado(MiembroComunidad):
    
    def __init__(self,pn="",pc="",ps=0.0):
         super().__init__(pn)
         self.cedula = pc
         self.salario = ps

    def Imprimir(self):
        super().Imprimir()
        print("Cedula :",self.cedula)
        print("Salario :",self.salario)
    
class Estudiante(MiembroComunidad):
    def __init__(self,pn="",pt="",pa=""):
         super().__init__(pn)
         self.tipo = pt ##presencial o autodidacta
         self.asignatura = pa
         
    def Imprimir(self):
        super().Imprimir()
        print("Tipo :",self.tipo)
        print("Asignatura :",self.asignatura)
        
class Alumno(MiembroComunidad):
    def __init__(self,pn="",pc="",pe=""):
        super().__init__(pn)
        self.carne = pc
        self.escuela = pe
    
    
    def Imprimir(self):
        super().Imprimir()
        print("Carné :",self.carne)
        print("Escuela :",self.escuela)
        
class AlumnoUniversidad(Alumno,Estudiante):
    def __init__(self,pn="",pt="presencial",pa="",pc="",pe=""):
        Alumno.__init__(self,pn,pc,pe)
        Estudiante.__init__(self,pn,pt,pa)
        
class Graduado(AlumnoUniversidad):
    def __init__(self,pn="",pt="",pa="",pc="",pe="",pan=0,pg=""):
        super().__init__(pn,pt,pa,pc,pe)
        self.año=pan
        self.titulo=pg
    
    def Imprimir(self):
        super().Imprimir()
        print("Año :",self.año)
        print("Título académico :",self.titulo) 

class Administrador(Empleado):

    def __init__(self,pn="",pc="",ps=0.0,pd=""):
        super().__init__(pn,pc,ps)
        self.departamento = pd

    def Imprimir(self):
        super().Imprimir()
        print("Departamento :",self.departamento)
    
class Profesor(Empleado):
    def __init__(self,pn="",pc="",ps=0.0,pm=""):
        super().__init__(pn,pc,ps)
        self.materia = pm

    def Imprimir(self):
        super().Imprimir()
        print("Materia :",self.materia)

class ProfesorAdministrador(Administrador,Profesor):
    def __init__(self,pn="",pc="",ps=0.0,pd="",pm=""):
        Administrador.__init__(self,pn,pc,ps,pd)
        Profesor.__init__(self,pn,pc,ps,pm)
        

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

pa = ProfesorAdministrador("Roberto Mena","5",600000.0,"Dep. Deocente","Matematica")
pa.Imprimir()
print()
e1=Estudiante("Melisa","Inactivo","Algrebra")
e1.Imprimir()
print()
a1 = Alumno("Juno solari","304750482","Colegio RT")
a1.Imprimir()
print()
u1 = AlumnoUniversidad("Junito Mora","Virtual","Elementos","558-896","TEC")
u1.Imprimir()
print()
g1 = Graduado("Alvaro Rojas","Presencial", "nulo","2013101764", "Ulatina",2018,"Licenciado en Nadalogía")
g1.Imprimir()

