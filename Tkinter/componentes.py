import tkinter as tk
from time import sleep
from tkinter import ttk, messagebox, scrolledtext

class ComponentesVentana(tk.Tk):
    def __init__(self):
        #siempre inicializar elcomponente de la clase padre
        super().__init__()
        self.geometry('650x400+450+200')
        self.title('Componentes')
        self.iconbitmap('icono.ico')
        self._crear_tabs()
    def _crear_componentes_tabulador1(self,tabulador):
        #agregamos una eqtiqueta y un componente de entrada
        etiqueta1 = ttk.Label(tabulador,text='Nombre:')
        etiqueta1.grid(row=0,column=0,sticky=tk.E)
        entrada1=ttk.Entry(tabulador,width=30)
        entrada1.grid(row=0,column=1,padx=5,pady=5)
        def enviar():
            messagebox.showinfo('Mensaje', f'Nombre:{entrada1.get()}')
        #agregamos un boton
        boton1=ttk.Button(tabulador,text='Enviar',command=enviar)
        boton1.grid(row=1,column=0,columnspan=2,padx=5,pady=5)
    def _crear_componentes_tabulador2(self,tabulador):
        contenido='Este es mi texto con el contenido'
        #creamos el componente de scroll
        scroll = scrolledtext.ScrolledText(tabulador,width=50,height=20,wrap=tk.WORD)
        scroll.insert(tk.INSERT,contenido)
        scroll.grid(row=0,column=0)
    def _crear_componentes_tabulador3(self,tabulador):
        #creamos una lista usando datalist comprehensions
        datos=[x+1 for x in range(10)]
        combobox=ttk.Combobox(tabulador,width=15,values=datos)
        combobox.grid(row=0,column=0,padx=5,pady=5)
        #seleccionamos un elemento a default por mostrar
        combobox.current(0)
        #agregamos un boton para saber que opcion se selecciono
        def mostrar_valor():
            messagebox.showinfo('Mensaje', f'Valor seleccionado:{combobox.get()}')
        boton1= ttk.Button(tabulador,text='Mostrar Valor Seleccionado',command=mostrar_valor)
        boton1.grid(row=0,column=1)
    def _crear_componentes_tabulador4(self,tabulador):
        imagen=tk.PhotoImage(file='python-logo.png')
        def mostrar_nombre_imagen():
            messagebox.showinfo('Mas info de la imagen', f'Nombre de imagen:{imagen.cget('file')}')
        boton_imagen=ttk.Button(tabulador,image=imagen,command=mostrar_nombre_imagen)
        boton_imagen.grid(row=0,column=0)
    def _crear_componentes_tabulador5(self,tabulador):
        #creamos el componentes de barra de progreso
        barra_progreso=ttk.Progressbar(tabulador,orient=tk.HORIZONTAL,length=550)
        barra_progreso.grid(row=0,column=0,padx=10,pady=10,columnspan=4)
        #botones para controlar los eventos de la barra de
        def ejecutar_barra():
            barra_progreso['maximum'] = 100
            for valor in range(101):
                #mandamos a esperar un poco antes de continuar con la ejecucion de la barra
                sleep(0.05)
                #incrementamos nuestra barra de progreso
                barra_progreso['value'] = valor
                #actualizamos la barra de progreso
                barra_progreso.update()
            barra_progreso['value'] = 0
        def ejecutar_ciclo():
            barra_progreso.start()
        def detener_ciclo():
            barra_progreso.stop()
        def detener_despues():
            esperar_ms=1000
            #detiene la ejecucion de un componente despues de ciertos ms
            self.after(esperar_ms,barra_progreso.stop)
        boton_inicio=ttk.Button(tabulador,text='Ejecutar Barra de progreso',command=ejecutar_barra)
        boton_inicio.grid(row=1,column=0)
        #creamos el boton de ciclo
        boton_ciclo=ttk.Button(tabulador,text='Ejecutar ciclo',command=ejecutar_ciclo)
        boton_ciclo.grid(row=1,column=1)
        boton_deter=ttk.Button(tabulador,text='Detener Ejecucio',command=detener_ciclo)
        boton_deter.grid(row=1,column=2)
        boton_despues=ttk.Button(tabulador,text='Detener Ejecucion Despues',command=detener_despues)
        boton_despues.grid(row=1,column=3)
    def _crear_tabs(self):
        #creamos un tab control,para ello usamos la clase de notebook
        control_tabulador = ttk.Notebook(self)
        #agregamos un frame o marco para agregar dentro del tabulador y organizar los elementos que agregemos dentro del tabulador
        tabulador1= ttk.Frame(control_tabulador)
        #agregamos este nuevo tabulador al control de tabuladores
        control_tabulador.add(tabulador1,text='Tabulador 1')
        #mostramos el tabulador
        control_tabulador.pack(fill='both')
        #crear componentes tabulador
        self._crear_componentes_tabulador1(tabulador1)
        #creamos un segundo tabulador
        tabulador2=ttk.LabelFrame(control_tabulador,text='Contenido')
        control_tabulador.add(tabulador2,text='Tabulador 2')
        #Creamos los componentes del segundo tabulador
        self._crear_componentes_tabulador2(tabulador2)
        #crear un tercer tabulador
        tabulador3 = ttk.Frame(control_tabulador)
        control_tabulador.add(tabulador3,text='Tabulador 3')
        #creamos los componentes del tercer tabulador
        self._crear_componentes_tabulador3(tabulador3)
        #creamos el tabulador 4
        tabulador4 = ttk.LabelFrame(control_tabulador,text='Imagen')
        control_tabulador.add(tabulador4,text='Tabulador 4')
        #creamos los componentes del cuarto tabulador
        self._crear_componentes_tabulador4(tabulador4)
        #creamos un tabulador 5
        tabulador5=ttk.LabelFrame(control_tabulador,text='Progress bar')
        control_tabulador.add(tabulador5,text='Tabulador 5')
        #creamos los componentes del quinto tabulador
        self._crear_componentes_tabulador5(tabulador5)

if __name__ == '__main__':
    componentes_ventana = ComponentesVentana()
    componentes_ventana.mainloop()
    #preubaaaaa

