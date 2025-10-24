
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

#creamos una ventana
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.configure(bg='#1d2d44')
ventana.title('Manejo de Tabla')
#configuramos el grid
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1,weight=0)

#definir un estilo
estilos = ttk.Style()
estilos.theme_use('clam') #prepara el manejo del tema oscuro
estilos.configure('Treeview', background='black',
                   foreground='white',
                   fieldbackground='black',
                   rowheight=30)
estilos.map('Treeview',background=[('selected','#3a86ff')])

#definir las columnas
columnas=('Id','Nombre','Edad')
#con treeview creamos la tabla
tabla=ttk.Treeview(ventana,columns=columnas,show='headings')
#cabeceros a la tabla
tabla.heading('Id', text='ID',anchor=tk.CENTER)
tabla.heading('Nombre', text='NOMBRE',anchor=tk.W)
tabla.heading('Edad', text='EDAD',anchor=tk.W)
#informacion que tendra la tabla
#formato a las columnas
tabla.column('Id',width=80)
tabla.column('Nombre',width=120)
tabla.column('Edad',width=120)
#cargar datos a la tabla
datos=((1,'Alejandra',25),(2,'Daniela',34)) + ((1,'Alejandra',25),(2,'Daniela',34))+((1,'Alejandra',25),(2,'Daniela',34))+((1,'Alejandra',25),(2,'Daniela',34))+((1,'Alejandra',25),(2,'Daniela',34))+((1,'Alejandra',25),(2,'Daniela',34))
for persona in datos:
    tabla.insert(parent='',index=tk.END,values=persona)
#agregamos un scrollbar
scrollbar=ttk.Scrollbar(ventana,orient=tk.VERTICAL,command=tabla.yview)
tabla.configure(yscroll=scrollbar.set)
scrollbar.grid(row=0,column=1,sticky=tk.NS)
#Mostrar registro seleccionado
def mostrar_registro_seleccionado(event):
    #print('Ejecutando metodo mostrar-registro-seleccionado')
    elemento_seleccionado = tabla.selection()[0]#solo procesamos el primer registro
    elemento = tabla.item(elemento_seleccionado) #i9tem
    persona = elemento['values']#tupla de persona seleccionada
    print(persona)
    showinfo(title='Persona Seleccionada',message=f'{persona}')
#asociar el evento selct en la tabla
tabla.bind('<<TreeviewSelect>>',mostrar_registro_seleccionado)

#publicamos la tabla
tabla.grid(row=0,column=0,sticky='nsew')
ventana.mainloop()