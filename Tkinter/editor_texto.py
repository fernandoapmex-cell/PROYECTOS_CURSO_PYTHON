import  tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename


class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('GlobalMentoring.com.mx - Editor Texto')
        #configuracion de tamaño minimo de ventana
        self.rowconfigure(0,minsize=600,weight=1)
        #configuracion minima de la segunda columna
        self.columnconfigure(1,minsize=600,weight=1)
        #atributo de campo de texto
        self.campo_texto=tk.Text(self,wrap=tk.WORD)
        #atributo de archvo
        self.archivo = None
        #atributo para saber si ya se abrio un archivo anteriormente
        self._archivo_abierto=False
        #creacion de componentes de nuestra aplicacion
        self._crear_componentes()
        #creamos el menu
        self._crear_menu()
    def _crear_menu(self):
        #creamos el menu de la app
        menu_app=tk.Menu(self)
        self.config(menu=menu_app)
        #agregamos las opcions a nuestro menu
        #agregamos menu archvo
        menu_archivo=tk.Menu(menu_app,tearoff=False)
        menu_app.add_cascade(label='Archivo',menu=menu_archivo)
        #agregamos las opciones del menu archivo
        menu_archivo.add_command(label='Abrir',command=self._abrir_archivo)
        menu_archivo.add_command(label='Guardar',command=self._guardar)
        menu_archivo.add_command(label='Guardar como...',command=self._guardar_como)
        menu_archivo.add_separator()
        menu_archivo.add_command(label='Salir',command=self.quit)
    def _crear_componentes(self):
        frame_botones=tk.Frame(self,relief=tk.RAISED,bd=2)
        boton_abrir=tk.Button(frame_botones,text='Abrir',command=self._abrir_archivo)
        boton_guardar=tk.Button(frame_botones,text='Guardar',command=self._guardar)
        boton_guardar_como=tk.Button(frame_botones,text='Guardar como...',command=self._guardar_como)
        #los botones los vamos a expandir de manera horizontal(sticky 'ew')
        boton_abrir.grid(row=0,column=0,sticky=tk.EW,padx=5,pady=5)
        boton_guardar.grid(row=1,column=0,sticky=tk.EW,padx=5,pady=5)
        boton_guardar_como.grid(row=2,column=0,sticky=tk.NSEW,padx=5,pady=5)
        #se coloca el frame de manera vertical
        frame_botones.grid(row=0,column=0,sticky=tk.NS)
        #agregamos el campo de texto que se expandira por completo en el espacio
        self.campo_texto.grid(row=0,column=1,sticky=tk.NSEW)
    def _abrir_archivo(self):
        #abrimos el archivo para edicion(lectura escritura) askmode es para sacar el cuadrito de elegir que documento y r+ para leer y poder escribir
        self._archivo_abierto = askopenfile(mode='r+')
        #eliminamos el texto anterior en la caja de texto
        self.campo_texto.delete(1.0,tk.END)
        #Revisamos si hay un archivo
        if not self._archivo_abierto:
            return
        #abrimos el archivo en modo lectura/escritura como un recurso
        with open(self._archivo_abierto.name, mode='r') as self.archivo:
            #leemos el contenido del archivo
            texto=self.archivo.read()
            #insertamos el contenido a el campo de texto
            self.campo_texto.insert(1.0,texto)
            #modificamos el titulo de la aplicacion
            self.title(f'*Editor Texto: {self.archivo.name}')

    def _guardar(self):
        #revisamos si ya se abrio previamente un archivo
        if self._archivo_abierto:
            #salvamos el archivo(lo abrimos en modo escritura)
            with open(self._archivo_abierto.name,'w')as self.archivo:
                #leemos el contenido de la caja de texto
                texto=self.campo_texto.get(1.0,tk.END)
                #escribimos el contenido al mismo archivo
                self.archivo.write(texto)
                #cambiamos el nombre del titulo de la app
                self.title(f'Editor Texto: {self.archivo.name}')
        else:
            self._guardar_como()
    def _guardar_como(self):
        #salvamos el archivo actual como un nuevo archivo
        self.archivo=asksaveasfilename(defaultextension='txt',filetypes=[('Archivos de Texto','*.txt'),('Todos los archivos','*.*')])
        if not self.archivo:
            return
        #Abrimos el archivo si es un archivo valido en modo escrituro W = write
        with open(self.archivo,'w') as self.archivo:
            #leemos el contenido de la caja de texto
            texto = self.campo_texto.get(1.0, tk.END)
            # escribimos el contenido al mismo archivo
            self.archivo.write(texto)
            # cambiamos el nombre del titulo de la app
            self.title(f'Editor Texto: {self.archivo.name}')
            #indicamos que ya hemos abierto un archivo
            self._archivo_abierto = self.archivo
if __name__ == '__main__':
    editor=Editor()
    editor.mainloop()