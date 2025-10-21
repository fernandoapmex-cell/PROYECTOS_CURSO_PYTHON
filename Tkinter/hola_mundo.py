#GUI - Grafical User Interface
#Tkinter  - tk interface
#importamos el modulo de tkinter
import tkinter as tk
#importamos los componentes
from tkinter import ttk

#creamos un objeto usando la clase tk
ventana=tk.Tk()
#modificamos el tamaño de la ventana(pixeles)
ventana.geometry("600x400")
#cambiamos el nombre de la ventana
ventana.title('Hola Mundo')
#cambiamos icono de la barra de titulo
ventana.iconbitmap('icono.ico')
def evento_click():
    #cambiar texto del boton al click
    boton1.config(text='Boton Presionado')
    print('Ejecucion del evento_CLick')
    #creamos un nuevo componente al click
    boton2 = ttk.Button(ventana, text='Nuevo Boton')
    boton2.pack()
#creamos un boton (componente o widget),especificamos el padre del objeto (ventana)
boton1 = ttk.Button(ventana,text='Dar Click',command=evento_click)
#utilizar el pack layout manager para mostrar el boton de la ventana
boton1.pack()
#iniciamos la ventana(estya linea la ejecutamos la final para que se muestre la ventana
#si la ejecutamos antes no se van a mostrar los cambios
ventana.mainloop()