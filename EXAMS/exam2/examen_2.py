# coding=utf-8

#########################################################
#///////////////////////////////////////////////////////#
#########################################################
#########################################################
#   PROYECTO: Examen 2
#
#   FECHA: 3/08/20
#
#   VERSION: 0.0.0.1
#
#   CREADO POR: Emmanuel Rodriguez Bejarano
########################################################### 

###########################################################
#//////////////////Funcion Principal//////////////////////#
###########################################################

#from tkinter import *
import tkinter as tk

##se organiza  la ventana dentro de una clase para facilitar
## la modificacion de datos en los widgets y gestion de los
## mismos sin utilizar duplicacion/super posicion de widgets

class Interfaz():
    def __init__(self):
        self.ventana = tk.Tk()

        #logo de aplicacion
        ##logo creado con <a href='https://www.freepik.com/vectors/logo'>Logo vector created by freepik - www.freepik.com</a>
        self.logo = tk.PhotoImage(file='favicon-96x96.png')

        self.ventana.title("MiControl")
        self.ventana.geometry("800x600")
        self.ventana.iconphoto(False, self.logo) ##logo para thumbnail de la app
        self.ventana.configure(background='#a6d9d2')

        #labels de seccion
        self.t1 = tk.Label(self.ventana,
                           text="Medición de parámetros",
                           height=7,
                           width=80,
                           bg='#e9ff7c',
                           anchor='n')
        
        self.t2 = tk.Label(self.ventana,
                           text="Información de la máquina",
                           height=23,
                           width=70,
                           bg='#c0ffad',
                           anchor="nw",
                           padx = 10,
                           pady = 10)
        
        self.t3 = tk.Label(self.ventana,
                           text="Equipos disponibles",
                           height=23,
                           width=18,
                           anchor = "n",
                           bg='#ffc1ad',
                           padx = 10,
                           pady = 10)
        
        #logo interno
        self.l1 = tk.Label(self.ventana,
                           image=self.logo)

        #botones
        self.b1 = tk.Button(self.ventana,
                            text="Maquina 1",
                            height=2,
                            width=10,
                            command=self.bMaquina1)
        
        self.b2 = tk.Button(self.ventana,
                            text="Maquina 2",
                            height=2,
                            width=10,
                            command=self.bMaquina2)
        
        self.b3 = tk.Button(self.ventana,
                            text="Maquina 3",
                            height=2,
                            width=10,
                            command=self.bMaquina3)
        
        #llamar maquina1 por default
        self.maquina = self.cargaMaquina("archivo1")

        #imagen de maquina
        self.img1 = tk.Label(self.ventana, image=self.maquina["imagen"],
                             height=300,
                             width=562)
        
        ##descripcion de equipo
        self.d1 = tk.Label(self.ventana,
                           text=self.maquina["descripcion"],
                           height=3, width=70,
                           bg='lightgrey',
                           wraplength=560,
                           justify="left")

        ##mediciones
        #actual
        medicionesBg = "#ececec"
        medicionesBg2 = "#cdcdcd"
        self.m1a = tk.Label(self.ventana,
                            text="Medida Actual",
                            height=1, width=20,
                            bg=medicionesBg2)        
        self.m1b = tk.Label(self.ventana,
                            text=self.maquina["actual"],
                            height=3, width=20,
                            bg=self.maquina["estado"])

        #estado
        self.m2a = tk.Label(self.ventana,
                            text="Estado",
                            height=1, width=20,
                            bg=medicionesBg2)
        self.m2b = tk.Label(self.ventana,
                            image=self.maquina["estadoImg"],
                            height=53, width=162,
                            bg=medicionesBg)

        #limites de valores
        
        self.l0a = tk.Label(self.ventana,
                            text="Límites",
                            height=1, width=30,
                            bg=medicionesBg2)

        self.l1a = tk.Label(self.ventana,
                            text="Máximo",
                            height=1, width=10,
                            bg=medicionesBg)
        self.l1b = tk.Label(self.ventana,
                            text=self.maquina["maximo"],
                            height=2, width=10,
                            bg='pink',
                            borderwidth = 2,
                            relief='solid')
    
        self.l2a = tk.Label(self.ventana,
                            text="Meta",
                            height=1, width=10,
                            bg=medicionesBg)
        self.l2b = tk.Label(self.ventana,
                            text=self.maquina["meta"],
                            height=2, width=10,
                            bg='lightgreen',
                            borderwidth = 2,
                            relief='solid')
        
        self.l3a = tk.Label(self.ventana,
                            text="Mínimo",
                            height=1, width=10,
                            bg=medicionesBg)
        self.l3b = tk.Label(self.ventana,
                            text=self.maquina["minimo"],
                            height=2, width=10,
                            bg='pink',
                            borderwidth = 2,
                            relief='solid')
        
        ####################################################################
        ##llamado de widgets e insercion de los mismos en posicion definida
        ##labels de grupo
        self.t1.place(x=20,y=462,anchor='nw')
        
        self.t2.place(x=20,y=30,anchor='nw')

        self.t3.place(x=615,y=30,anchor='nw')


        ##logo
        self.l1.place(x=(800-115),y=(575),anchor='sw')

        ##botones
        self.b1.place(x=698,y= 120,anchor='center')

        self.b2.place(x=698,y= 250,anchor='center')

        self.b3.place(x=698,y= 380,anchor='center')

        ##imagen central
        self.img1.place(x=29,y=75,anchor="nw")

        ##descripcion
        self.d1.place(x=29,y=377,anchor='nw')

        ##etiquetas de mediciones
        ##actual
        m1y = 495
        m1x = 52
        self.m1a.place(x=m1x,y=m1y,anchor='nw')
        #valor
        self.m1b.place(x=m1x,y=m1y+21,anchor='nw')

        #estado
        m2y = m1y
        m2x = m1x + 164
        self.m2a.place(x=m2x,y=m2y,anchor='nw')
        #valor
        self.m2b.place(x=m2x,y=m2y+21,anchor='nw')

        #limites
        l0y =  m2y
        l0x = m2x + 164
        self.l0a.place(x=l0x,y=l0y,anchor='nw')
        #etiqueta maximo
        self.l1a.place(x=l0x,y=l0y+21,anchor='nw')
        #valor
        self.l1b.place(x=l0x,y=l0y+38,anchor='nw')
        #etiqueta meta
        self.l2a.place(x=l0x+80,y=l0y+21,anchor='nw')
        #valor
        self.l2b.place(x=l0x+80,y=l0y+38,anchor='nw')
        #etiqueta minimo
        self.l3a.place(x=l0x+160,y=l0y+21,anchor='nw')
        #valor
        self.l3b.place(x=l0x+160,y=l0y+38,anchor='nw')


        ##creacion de la ventana al final del proceso
        self.ventana.mainloop()


    #funcion llamado de datos
    def lDatos(self,filename):
        datos = open(filename,"r")
        lineas = datos.readlines()

        diccionario = {
            "imagen":lineas[0].split('\n')[0], ##remueve el terminador de linea \n
            ## y de esta manera evita errores al llamar el archivo.
            ##split() devuelve una lista, por lo que se toma solo el resultado en la
            ##posicion 0
            "descripcion":lineas[1],
            "actual":float(lineas[2]),
            "maximo":float(lineas[3]),
            "meta":float(lineas[4]),
            "minimo":float(lineas[5]),
            "estado":"",
            "estadoImg": ""
            }
        diccionario["imagen"] = tk.PhotoImage(file=diccionario["imagen"])

        ##en el enunciado no se solicita ningun comportamiento especifico
        ##para valores superiores al maximo
        if diccionario["actual"] <= diccionario["minimo"]:
            diccionario["estado"] = "#ffc5c3"
            diccionario["estadoImg"] = tk.PhotoImage(file="estado1x53.png")
        elif diccionario["actual"] > diccionario["minimo"] and diccionario["actual"] < diccionario["meta"]:
            diccionario["estado"] = "#fcff9b"
            diccionario["estadoImg"] = tk.PhotoImage(file="estado2x53.png")
        else:
            diccionario["estado"] = "#c6ffc3"
            diccionario["estadoImg"] = tk.PhotoImage(file="estado3x53.png")
        

        datos.close

        return diccionario

##funciones para los botones
    def bMaquina1(self):
        self.maquina = self.cargaMaquina("archivo1")
        self.actualizarGUI()

    def bMaquina2(self):
        self.maquina = self.cargaMaquina("archivo2")
        self.actualizarGUI()

    def bMaquina3(self):
        self.maquina = self.cargaMaquina("archivo3")
        self.actualizarGUI()

##funcion para llamar un archivo de datos
    def cargaMaquina(self,archivo):
        maquina = self.lDatos(archivo+".txt")
        return maquina

#funcion encargada de actualizar la pantalla
    def actualizarGUI(self):
        self.img1.configure(image=self.maquina["imagen"])
        self.d1.configure(text=self.maquina["descripcion"])
        self.m1b.configure(text=self.maquina["actual"])
        self.m1b.configure(bg=self.maquina["estado"])
        self.m2b.configure(image = self.maquina["estadoImg"])
        self.l1b.configure(text=self.maquina["maximo"])
        self.l2b.configure(text=self.maquina["meta"])
        self.l3b.configure(text=self.maquina["minimo"])
    


##iniciar interfaz y aplicacion
app = Interfaz()


