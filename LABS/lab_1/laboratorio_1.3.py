# coding=utf-8

#nice git info https://rogerdudler.github.io/git-guide/
#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 1.3
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



##The following are totally acceptable in python:
##
##passing a string representation of an integer into int
##passing a string representation of a float into float
##passing a string representation of an integer into float
##passing a float into int
##passing an integer into float
##But you get a ValueError if you pass a string representation of a float into int,
##or a string representation of anything but an integer (including empty string).
##If you do want to pass a string representation of a float to an int, as @katyhuff
##points out above, you can convert to a float first, then to an integer
##
##https://stackoverflow.com/questions/1841565/valueerror-invalid-literal-for-int-with-base-10
#while True:
try:
    num1 = int(input("Ingrese el divisor: "))
    print("110/",num1," = ","%.2f" % (110/num1))
except NameError:
    print("Error: El valor digitado no es un numero")
except ZeroDivisionError:
    print("Error: No se puede dividir por 0.")
except ValueError:
    print("Error: Debe ingresar un numero entero.")

