import tkinter as tk
from dataclasses import field
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Login')
ventana.configure(background='#1d2d44')
#configuramos le grid de la ventana
ventana.columnconfigure(0,weight=1)
ventana.rowconfigure(0,weight=1)
#creamos un estilo
estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure(ventana,background='#1d2d44',
                  foreground='white',
                  fieldbackground='black')
estilos.configure('TButton',background='#005f73')
estilos.map('TButton',background=[('active','#0a9396')])
#agregamos un frame
frame = ttk.Frame(ventana)
frame.columnconfigure(0,weight=1)
frame.columnconfigure(1,weight=3)
#titulo
etiqueta_titulo=ttk.Label(frame,text='Login',font=('Arial',20,'bold'))
etiqueta_titulo.grid(row=0,column=0,columnspan=2)
#usuario
usuario_etiqueta=ttk.Label(frame,text='Usuario :',font=('Arial',10))
usuario_etiqueta.grid(row=1,column=0,sticky=tk.W,padx=5,pady=5)
#usuario caja texto
usuario_caja_texto=ttk.Entry(frame)
usuario_caja_texto.grid(row=1,column=1,sticky=tk.E,padx=5,pady=5)

#password
password_etiqueta=ttk.Label(frame,text='Password :',font=('Arial',10))
password_etiqueta.grid(row=2,column=0,sticky=tk.W,padx=5,pady=5)
#password caja texto
password_caja_texto=ttk.Entry(frame,show='*')
password_caja_texto.grid(row=2,column=1,sticky=tk.E,padx=5,pady=5)

#boton login
login_boton=ttk.Button(frame,text='Enviar')
login_boton.grid(row=3,column=0,columnspan=2,padx=5,pady=5)
#metodos
def validar(event):
    usuario= usuario_caja_texto.get()
    password= password_caja_texto.get()
    #root usuario y admin password es correcto
    if usuario == 'root' and password == 'admin':
        messagebox.showinfo(title='Login ',message='Datos Correctos!')
    else:
        messagebox.showerror(title='Login ',message='Usuario Incorrecto!')

#asociar eventos al boton de login
login_boton.bind('<Return>',validar) #presionar la tecla de enter
login_boton.bind('<Button-1>',validar) #capturar el evento click izquiero del mouse



#imprimir
frame.grid(row=0,column=0)
ventana.mainloop()