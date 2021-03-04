# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 3.4
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

##finalizar cono, cilindro y piramide con area y volumen


##ejemplo
def biblioteca(l,r,i):
    return l*500 + r*100*l + (2000 if i else 0) ##ternary

#programa
libros = int(input("Indique la cantidad de libros:"))
retraso = int(input("Indique los dias de retraso:"))
inscripcion = (input("Requiere inscripcion? (si o no):"))
if (inscripcion == "si"):
    inscripcion = True
else:
    inscripcion = False


print()
print("Debe pagar:", biblioteca(libros,retraso,inscripcion))

