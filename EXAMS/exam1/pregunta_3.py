# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Examen pregunta 3
#
#   FECHA: 28/05/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
#
###########################################################

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################
def sumaPar (A, B):
    return A+B


n = eval(input("Indique el tamaño de la lista: "))

listaA = []
listaB = []
listaC = []


##metodo 1, ya habia hecho el metodo 2 antes de recibir el mensaje
##------------- ／＞　フ
##-------------| _　_|
##----------／` ミ＿xノ
##--------/　　 　　 |
##-------/　 ヽ　　 ﾉ

##for i in range(n):
##    A = (eval(input("Valor A%d: " % i+1)))
##    B = (eval(input("Valor B%d: " % i+1)))
##    listaA.append(A)
##    listaB.append(B)
##    listaC.append(A+B)

##metodo con posiciones
for i in range(n):
    A = (eval(input("Valor A%d: " %(i+1))))
    B = (eval(input("Valor B%d: " %(i+1))))
    listaA.append(A)
    listaB.append(B)

for j in range(len(listaA)): ##en lugar de de len(listaA) puede ser n, es igual
    listaC.append(listaA[j] + listaB[j])



print("La lista A es: ")
print(listaA)
print("La lista B es: ")
print(listaB)
print("La lista C es: ")
print(listaC)
