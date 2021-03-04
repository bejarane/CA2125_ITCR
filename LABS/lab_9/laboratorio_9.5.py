# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 9.5
#
#   FECHA: 16/06/20
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

#se asume que matriz es cuadrada y etcetera, multiplicacion permite matrices desiguales
#clases / concepto
class Matriz:
    m = []

    def SetMatriz(self,pm):
        self.m = pm

    def GetMatriz(self):
        pass

    def Suma(self,m2):
        fil1 = len(self.m)
        fil2 = len(m2.m)
        col1 = len(self.m[0])
        col2 = len(m2.m[0])

        if (fil1 == fil2 and col1 == col2): ##iguales
            mr = []
            for j in range(fil1):
                mr.append([])
                for i in range(col1):
                    mr[j].append(self.m[j][i]+m2.m[j][i])
            return mr
        else:
            print("Error, matrices no compatibles")

    def Multiplicar(self,m2):
        fil1 = len(self.m)
        fil2 = len(m2.m)
        col1 = len(self.m[0])
        col2 = len(m2.m[0])

        if (col1 == fil2): ##compatibles
            mr = []
            for j in range(fil1):
                mr.append([])
                for i in range(col2):
                    suma = 0
                    for k in range(col1):
                        suma+= self.m[j][k] * m2.m[k][i]
                    mr[j].append(suma)
            return mr
        else:
            print("Error, matrices no compatibles")

#programa
m1 = Matriz()
m1.SetMatriz([[1,2,3],[4,5,6]])

mat2 = [[1,2,3],[4,5,6]]
m2 = Matriz()
m2.SetMatriz(mat2)

print("suma")
print(m1.Suma(m2))



#matrices nuevas para prueba de multiplicacion
m1 = Matriz()
m1.SetMatriz([[1,2,3],[4,5,6]])

mat2 = [[1,2,3],[1,2,3],[1,2,3]]
m2 = Matriz()
m2.SetMatriz(mat2)

print("multiplicacion")
print(m1.Multiplicar(m2))
