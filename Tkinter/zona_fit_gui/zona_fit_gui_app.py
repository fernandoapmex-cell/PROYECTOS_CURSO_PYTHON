import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo
from Tkinter.zona_fit_gui.cliente import Cliente
from Tkinter.zona_fit_gui.cliente_dao import ClienteDAO


class App(tk.Tk):
    COLOR_VENTANA ='#1d2d44'
    def __init__(self):
        self._id_cliente=None
        super().__init__()
        self.configurar_ventana()
        self.configurar_grid()
        self.mostrar_formulario()
        self.cargar_tabla()
        self.mostrar_botones()
    def configurar_ventana(self):
        self.geometry('700x500')
        self.title('Zona Fit App')
        self.configure(background=App.COLOR_VENTANA)
        #aplicamos el estilo
        self.estilos=ttk.Style()
        self.estilos.theme_use('clam') # preparamos los estulos para el modo oscuro
        self.estilos.configure(self,background=App.COLOR_VENTANA,foreground='white',fieldbackground='black')
    def configurar_grid(self):
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=1)
        self.mostrar_titulo()
    def mostrar_titulo(self):
        etiqueta = ttk.Label(self, text='Zona Fit (GYM)',font=('Arial',15),background=App.COLOR_VENTANA,foreground='white')
        etiqueta.grid(column=0,row=0,columnspan=2,pady=30)
    def mostrar_formulario(self):
        #ageegamos el frame para mostrar formulario
        self.frame_forma=ttk.Frame(self)
        #Nombre
        nombre_label = ttk.Label(self.frame_forma,text='Nombre :')
        nombre_label.grid(column=0,row=0,sticky=tk.W,pady=30,padx=5)
        self.nombre_entrada=ttk.Entry(self.frame_forma)
        self.nombre_entrada.grid(column=1,row=0)
        #Apellido
        apellido_label = ttk.Label(self.frame_forma,text='Apellido :')
        apellido_label.grid(column=0,row=1,sticky=tk.W,pady=30,padx=5)
        self.apellido_entrada=ttk.Entry(self.frame_forma)
        self.apellido_entrada.grid(column=1,row=1)
        #Membresia
        membresia_label = ttk.Label(self.frame_forma,text='Membresia :')
        membresia_label.grid(column=0,row=2,sticky=tk.W,pady=30,padx=5)
        self.membresia_entrada=ttk.Entry(self.frame_forma)
        self.membresia_entrada.grid(column=1,row=2)
        #publicamos el frame de la forma
        self.frame_forma.grid(column=0,row=1)
    def cargar_tabla(self):
        #creamos un frame para mostrar la tabla
        self.frame_tabla = ttk.Frame(self)
        #definimos los estilos de la tabla
        self.estilos.configure('Treeview',background='black',foreground='white',fieldbackground='black',rowconfigure=20)
        #definimos las columnas
        columnas = ('Id','Nombre','Apellido','Membresia')
        #creamos el objeto tabla
        self.tabla=ttk.Treeview(self.frame_tabla,columns=columnas,show='headings')
        #agregamos los cabeceros
        self.tabla.heading('Id',text='ID',anchor='center')
        self.tabla.heading('Nombre',text='NOMBRE',anchor=tk.W)
        self.tabla.heading('Apellido',text='APELLIDO',anchor=tk.W)
        self.tabla.heading('Membresia',text='MEMBRESIA',anchor=tk.W)
        #Definimos las columnas
        self.tabla.column('Id',anchor=tk.CENTER,width=50)
        self.tabla.column('Nombre',anchor=tk.W,width=100)
        self.tabla.column('Apellido',anchor=tk.W,width=100)
        self.tabla.column('Membresia',anchor=tk.W,width=100)
        #cargar los datos de la base de datos
        clientes=ClienteDAO.seleccionar()
        for cliente in clientes:
            self.tabla.insert('',index=tk.END,values=(cliente.id_cliente,cliente.nombre_cliente,cliente.apellido_cliente,cliente.membresia_cliente))
        # Agregamos el scrollbar
        scrollbar = ttk.Scrollbar(self.frame_tabla, orient=tk.VERTICAL,
                                  command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky=tk.NS)
        #asociar el evento select
        self.tabla.bind('<<TreeviewSelect>>',self.cargar_cliente)
        #mostramos la tabla
        self.tabla.grid(column=0,row=0)
        #mostramos le frame tabla
        self.frame_tabla.grid(column=1,row=1,padx=20)
    def mostrar_botones(self):
        self.frame_botones = ttk.Frame()
        #crear los botones
        agregar_boton=ttk.Button(self.frame_botones,text='Guardar',command=self.validar_cliente)
        agregar_boton.grid(column=0,row=0,padx=30)
        eliminar_boton=ttk.Button(self.frame_botones,text='Eliminar',command=self.eliminar_cliente)
        eliminar_boton.grid(column=1,row=0,padx=30)
        limpiar_boton=ttk.Button(self.frame_botones,text='Limpiar',command=self.limpiar_datos)
        limpiar_boton.grid(column=2,row=0,padx=30)
        #aplicar estilo a los botones
        self.estilos.configure('TButton',background='#005f73')
        self.estilos.map('TButton',background=[('active','#0a9396')])
        #publicar el frame de botones
        self.frame_botones.grid(column=0,row=2,columnspan=2,pady=20)
    def validar_cliente(self):
        #validar los campos
        if(self.nombre_entrada.get() and self.apellido_entrada.get() and self.membresia_entrada.get()):
            if self.validar_membresia():
                self.guardar_cliente()
            else:
                showerror(title='Atencion!',message='El valor de membresia no es numerico!')
                #asi limpiamos la entrada de membresia
                self.membresia_entrada.delete(0,'end')
                self.membresia_entrada.focus_set()
        else:
            showerror(title='Atencion!',message='Debe llenar el formulario!')
            self.nombre_entrada.focus_set()
    def eliminar_cliente(self):
        if self.id_cliente is None:
            showerror(title='Atencion!',message='Debes seleccionar un cliente para eliminar!')
        else:
            cliente=Cliente(id_cliente=self.id_cliente)
            ClienteDAO.eliminar(cliente)
            showinfo(title='Eliminado!',message='Cliente Eliminado exitosamente!')
            self.recargar_datos()
    def limpiar_datos(self):
        self.limpiar_formulario()
        self.id_cliente=None
    def validar_membresia(self):
        try:
            int(self.membresia_entrada.get())
            return True
        except Exception as e:
            #no es un valor numerico
            return False
    def guardar_cliente(self):
        #recuperamos los valores de las cajas de texto
        nombre = self.nombre_entrada.get()
        apellido = self.apellido_entrada.get()
        membresia = self.membresia_entrada.get()
        #validamos el atributo del id cliente para ver si vamos a guardar o actualizar
        if self.id_cliente is None:
            #agregar
            cliente =Cliente(nombre_cliente=nombre,apellido_cliente=apellido,membresia_cliente=membresia)
            ClienteDAO.insertar(cliente)
            showinfo(title='Agregar!',message='Cliente agregado...!')
        else:
            #actualizar
            cliente=Cliente(self.id_cliente,nombre,apellido,membresia)
            ClienteDAO.actualizar(cliente)
            showinfo(title='Actualizar!',message='Cliente actualizado...!')
        #volvemos a mostrar los datos y limpiamos el formulario
        self.recargar_datos()
    def cargar_cliente(self,event):
        elemento_seleccionado = self.tabla.selection()[0]
        elemento=self.tabla.item(elemento_seleccionado)
        cliente_valores=elemento['values'] #tupla de valores del cliente seleccionado
        #recuperar  cada valor del cliente
        self.id_cliente=cliente_valores[0]
        nombre_cliente=cliente_valores[1]
        apellido_cliente=cliente_valores[2]
        membresia_cliente=cliente_valores[3]
        #antes de agregar tenemos que limpiar el formulario
        self.limpiar_formulario()
        #cargar los valores en el formulario
        self.nombre_entrada.insert(0,nombre_cliente)
        self.apellido_entrada.insert(0,apellido_cliente)
        self.membresia_entrada.insert(0,membresia_cliente)
    def recargar_datos(self):
        #volver a cargar los datos de la tabla
        self.cargar_tabla()
        #limpiar los datos
        self.limpiar_datos()
    def limpiar_formulario(self):
        self.nombre_entrada.delete(0,'end')
        self.apellido_entrada.delete(0,'end')
        self.membresia_entrada.delete(0,'end')


if __name__ == '__main__':
    app = App()
    app.mainloop()
