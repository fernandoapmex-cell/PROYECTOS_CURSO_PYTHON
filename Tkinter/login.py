#ventana principal
import tkinter as tk
from tkinter import ttk,messagebox
class LoginVentana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('250x130')
        self.title('Login')
        self.iconbitmap('icono.ico')
        #bloquar tamaño
        self.resizable(0,0)
        #configuracion del grid
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=3)

        self._crear_componentes()

    #definir el metodo
    def _crear_componentes(self):
        #usuario
        usuario_etiqueta=ttk.Label(self, text='Usuario:')
        usuario_etiqueta.grid(row=0, column=0,sticky=tk.E,padx=5,pady=5)
        self.usuario_entrada=ttk.Entry(self, width=20)
        self.usuario_entrada.grid(row=0, column=1,sticky=tk.W,padx=5,pady=5)
        #password
        password_etiqueta=ttk.Label(self, text='Password:')
        password_etiqueta.grid(row=1, column=0,sticky=tk.E,padx=5,pady=5)
        self.password_entrada=ttk.Entry(self, width=20,show='*')
        self.password_entrada.grid(row=1, column=1,sticky=tk.W,padx=5,pady=5)
        #boton login
        login_boton=ttk.Button(self,text='Login',command=self._login)
        login_boton.grid(row=2, column=0,columnspan=2)

    #metodos
    def _login(self):
        messagebox.showinfo('Datos Login',f'Usuario:{self.usuario_entrada.get()},Password:{self.password_entrada.get()} ')

if __name__ == '__main__':
    login_ventana = LoginVentana()
    login_ventana.mainloop()