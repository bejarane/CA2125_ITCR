# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Laboratorio 14
#
#   FECHA: 23/07/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
########################################################### 

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

from tkinter import *

#funciones
def ColorVerde():
    color = Label(v1,image=iverde).place(x=20,y=20)

def ColorAmarillo():
    color = Label(v1,image=iamarilla).place(x=20,y=20)

def ColorRojo():
    color = Label(v1,image=irojo).place(x=20,y=20)

#programa
v1 = Tk()
v1.title("Uso de imagenes")
v1.geometry("500x500")

irojo = PhotoImage(file="rojo.GIF")
iverde = PhotoImage(file="verde.GIF")
iamarilla = PhotoImage(file="amarillo.GIF")

color  = Label(v1,image=iamarilla).place(x=20,y=20)
bverde = Button(v1,text="Verde",height=3,width=10,bg="green",command=ColorVerde).place(x=250,y=20)
bamarillo = Button(v1,text="Amarillo",height=3,width=10,bg="yellow",command=ColorAmarillo).place(x=250,y=100)
brojo = Button(v1,text="Rojo",height=3,width=10,bg="red",command=ColorRojo).place(x=250,y=180)

v1.mainloop()
