import sys
import tkinter as tk
from tkinter import ttk,messagebox,Menu

ventana=tk.Tk()

ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

#definimos una variable que podremos modificar posteriormente(set),leer(get)
entrada_var1=tk.StringVar(value='Valor por default')
#witdh cantidad de caracteres que ocupa la caja
entrada1=ttk.Entry(ventana,width=30,justify=tk.CENTER,textvariable=entrada_var1,state=tk.NORMAL)
entrada1.grid(row=0,column=0,sticky='NSWE')
#etiqueta o label
etiqueta1=tk.Label(ventana,text='Aqui se mostrara el contenido de la caja de texto')
etiqueta1.grid(row=1,column=0,columnspan=2,sticky='NSWE')
#insert agrega un texto
entrada1.insert(0,'Introduce una cadena de texto')
entrada1.insert(tk.END,'.')
#entrada1.configure(state='readonly')

#evento enviar
def enviar():
    #print(entrada1.get())
    #boton1.configure(text=entrada1.get())
    #eliminar contenido
    #entrada1.delete(0,tk.END)
    #seleccionar el texto de la caja
    #entrada1.select_range(0,tk.END)
    #hacer efectiva la seleccion
    #entrada1.focus()
    #recuperamos la informacion apartir de la variable asociada
    #boton1.configure(text=entrada_var1.get())
    #entrada_var1.set('Cambio...')
    #print(entrada_var1.get())
    #print(entrada1.get())
    #etiqueta1.config(text=entrada_var1.get())
    etiqueta1.config(text=entrada_var1.get())
    #messagebox(caja de mensaje)
    mensaje1=entrada1.get()
    if mensaje1:
        messagebox.showinfo('Mensaje Informativo :',mensaje1+'Informativo')
       # messagebox.showerror('Mensaje Error :',mensaje1+'Error')
       # messagebox.showwarning('Mensaje Warning :',mensaje1+'Warning')
def crear_menu():
    #configurar el menu principal
    menu_principal=Menu(ventana)
    #tearoff tiene que estar en falso para evitar que el menu se separe de la interfaz
    submenu_archivo = Menu(menu_principal,tearoff=False)
    #agregamos una nueva opcion al menu de archivo
    submenu_archivo.add_command(label='Nuevo')
    #agregar un separador
    submenu_archivo.add_separator()
    #agregamos opcion de salir
    submenu_archivo.add_command(label='Salir',command=salir)
    #agregamos el submenu al menu Salir
    menu_principal.add_cascade(menu=submenu_archivo,label='Archivo')
    #submenu Ayuda
    submenu_ayuda = Menu(menu_principal,tearoff=False)
    submenu_ayuda.add_command(label='Acerca De..')
    submenu_ayuda.add_separator()
    #agregamos el submenu al menu Salir
    menu_principal.add_cascade(menu=submenu_ayuda,label='Ayuda')
    #mostrar el menu en ventana principal
    ventana.config(menu=menu_principal)
def salir():
    ventana.quit()
    ventana.destroy()
    print('Salimos')
    sys.exit()
#cramos un boton
boton1=ttk.Button(ventana,text='Enviar',command=enviar)
boton1.grid(row=0,column=1,sticky='NSWE')
crear_menu()
ventana.mainloop()