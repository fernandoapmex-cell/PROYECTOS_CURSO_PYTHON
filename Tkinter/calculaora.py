import tkinter as tk
from tkinter import messagebox

class Calcualdora(tk.Tk):
    def __init__(self):
        # siempre que llamamos a tk llamamos al constructor de la clase padre
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title("Calculadora")
        self.iconbitmap('calculadora.ico')
        #atributos de clase
        self.expresion=""
        #caja de texto (input)
        self.entrada=None
        #variable asociada a la caja de entrada
        #stringVar lo vamos a usar para obtener el valor del input
        self.entrada_texto=tk.StringVar()
        #creamos los componentes
        self._creacion_componentes()
    #metodos de la clase
    #metodo para crear los componentes
    def _creacion_componentes(self):
        #creamos un frame
        entrada_frame=tk.Frame(self,width=400,height=50,bg='grey')
        entrada_frame.pack(side=tk.TOP)
        #caja de texto pongo que las letras que se metan ahi tendran esos parametros
        entrada=tk.Entry(entrada_frame,font=('arial',18,'bold'),textvariable=self.entrada_texto,width=30,justify=tk.RIGHT)
        entrada.grid(row=0,column=0,ipady=10)
        #creamos el segundo frame para los botones de la calculadora|
        botones_frame=tk.Frame(self,width=400,height=450,bg='grey')
        botones_frame.pack()
        #primer renglon
        boton_limpiar=tk.Button(botones_frame,text='C',width=32,height=3,bd=0,bg='#eee',cursor='hand2',command=self._evento_limpiar)
        boton_limpiar.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
        #boton dividir
        #usamos lamda para que no se mande a llamar la funcion y solo se ejecute al click
        boton_dividir=tk.Button(botones_frame,text='/',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:self._evento_click('/')).grid(row=0,column=4,padx=1,pady=1)
        #segundo renglon
        boton_siete=tk.Button(botones_frame,text='7',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:self._evento_click(7))
        boton_siete.grid(row=1,column=0,padx=1,pady=1)
        boton_ocho=tk.Button(botones_frame,text='8',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:self._evento_click(8))
        boton_ocho.grid(row=1,column=1,padx=1,pady=1)
        boton_nueve=tk.Button(botones_frame,text='9',width=10,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:self._evento_click(9))
        boton_nueve.grid(row=1,column=2,padx=1,pady=1)
        #boton Multiplicacion
        boton_multiplicar=tk.Button(botones_frame,text='*',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:self._evento_click('*')).grid(row=1,column=4,padx=1,pady=1)
        #tercer renglon
        boton_cuatro = tk.Button(botones_frame, text='4', width=10, height=3, bd=0, bg='#fff', cursor='hand2',command=lambda: self._evento_click(4))
        boton_cuatro.grid(row=2, column=0, padx=1, pady=1)
        boton_cinco = tk.Button(botones_frame, text='5', width=10, height=3, bd=0, bg='#fff', cursor='hand2',command=lambda: self._evento_click(5))
        boton_cinco.grid(row=2, column=1, padx=1, pady=1)
        boton_seis = tk.Button(botones_frame, text='6', width=10, height=3, bd=0, bg='#fff', cursor='hand2',command=lambda: self._evento_click(6))
        boton_seis.grid(row=2, column=2, padx=1, pady=1)
        #boton Resta
        boton_restar=tk.Button(botones_frame,text='-',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:self._evento_click('-')).grid(row=2,column=4,padx=1,pady=1)
        #cuarto renglon
        boton_uno = tk.Button(botones_frame, text='1', width=10, height=3, bd=0, bg='#fff', cursor='hand2',command=lambda: self._evento_click(1))
        boton_uno.grid(row=3, column=0, padx=1, pady=1)
        boton_dos = tk.Button(botones_frame, text='2', width=10, height=3, bd=0, bg='#fff', cursor='hand2',command=lambda: self._evento_click(2))
        boton_dos.grid(row=3, column=1, padx=1, pady=1)
        boton_tres = tk.Button(botones_frame, text='3', width=10, height=3, bd=0, bg='#fff', cursor='hand2',command=lambda: self._evento_click(3))
        boton_tres.grid(row=3, column=2, padx=1, pady=1)
        #boton Sumar
        boton_sumar=tk.Button(botones_frame,text='+',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:self._evento_click('+')).grid(row=3,column=4,padx=1,pady=1)
        #quinto renglon
        boton_cero=tk.Button(botones_frame,text='0',width=21,height=3,bd=0,bg='#fff',cursor='hand2',command=lambda:self._evento_click('0')).grid(row=4,column=0,columnspan=2,padx=1,pady=1)
        boton_punto=tk.Button(botones_frame,text='.',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=lambda:self._evento_click('.')).grid(row=4,column=2,padx=1,pady=1)
        boton_igual=tk.Button(botones_frame,text='=',width=10,height=3,bd=0,bg='#eee',cursor='hand2',command=self._evento_evaluar).grid(row=4,column=4,padx=1,pady=1)
    def _evento_evaluar(self):
        #eval evalua uan expresion string como aritmetica (int,float etc)
        try:
            if self.expresion:
                resultado=str(eval(self.expresion))
                self.entrada_texto.set(resultado)
        except Exception as e:
            messagebox.showerror("Error",f'Ocurrio un error : {e}')
            self.entrada_texto.set('')
        finally:
            self.expresion=''
    def _evento_limpiar(self):
        self.expresion=''
        self.entrada_texto.set(self.expresion)
    def _evento_click(self,elemento):
        #concatenamos el nuevo elemento a la expresion a existente
        self.expresion=f'{self.expresion}{elemento}'
        self.entrada_texto.set(self.expresion)
if __name__ == '__main__':
    calculadora = Calcualdora()
    calculadora.mainloop()