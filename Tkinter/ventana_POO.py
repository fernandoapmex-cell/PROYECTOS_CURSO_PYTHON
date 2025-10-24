import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


class App(tk.Tk):
    def __init__(self):
        super().__init__() # constructor de la clase padre
        #configurar la ventana
        self.configurar_ventana()
        #configurar el grid
        self.configurar_grid()
        #mostrar tabla
        self.mostrar_tabla()
    def configurar_ventana(self):
        self.geometry("600x400")
        self.configure(bg="#1d2d44")
        self.title("Manejo de ventanas con POO")
    def configurar_grid(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=0)
    def mostrar_tabla(self):
        # definir un estilo
        estilos = ttk.Style()
        estilos.theme_use('clam')  # prepara el manejo del tema oscuro
        estilos.configure('Treeview', background='black',
                          foreground='white',
                          fieldbackground='black',
                          rowheight=30)
        estilos.map('Treeview', background=[('selected', '#3a86ff')])
        # definir las columnas
        columnas = ('Id', 'Nombre', 'Edad')
        # con treeview creamos la tabla
        self.tabla = ttk.Treeview(self, columns=columnas, show='headings')
        # cabeceros a la tabla
        self.tabla.heading('Id', text='ID', anchor=tk.CENTER)
        self.tabla.heading('Nombre', text='NOMBRE', anchor=tk.W)
        self. tabla.heading('Edad', text='EDAD', anchor=tk.W)
        # informacion que tendra la tabla
        # formato a las columnas
        self.tabla.column('Id', width=80)
        self.tabla.column('Nombre', width=120)
        self.tabla.column('Edad', width=120)
        # cargar datos a la tabla
        datos = ((1, 'Alejandra', 25), (2, 'Daniela', 34)) + ((1, 'Alejandra', 25), (2, 'Daniela', 34)) + (
            (1, 'Alejandra', 25), (2, 'Daniela', 34)) + ((1, 'Alejandra', 25), (2, 'Daniela', 34)) + (
                    (1, 'Alejandra', 25), (2, 'Daniela', 34)) + ((1, 'Alejandra', 25), (2, 'Daniela', 34))
        for persona in datos:
            self.tabla.insert(parent='', index=tk.END, values=persona)
        # agregamos un scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        # asociar el evento selct en la tabla
        self.tabla.bind('<<TreeviewSelect>>',self.mostrar_registro_seleccionado)
        # publicamos la tabla
        self.tabla.grid(row=0, column=0, sticky='nsew')

    def mostrar_registro_seleccionado(self,event):
        # print('Ejecutando metodo mostrar-registro-seleccionado')
        elemento_seleccionado = self.tabla.selection()[0]  # solo procesamos el primer registro
        elemento = self.tabla.item(elemento_seleccionado)  # i9tem
        persona = elemento['values']  # tupla de persona seleccionada
        print(persona)
        showinfo(title='Persona Seleccionada', message=f'{persona}')


if __name__ == "__main__":

    app = App()
    app.mainloop()