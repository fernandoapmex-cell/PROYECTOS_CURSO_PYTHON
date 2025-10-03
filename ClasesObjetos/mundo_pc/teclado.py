from ClasesObjetos.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Teclado(DispositivoEntrada):
    contador_teclados = 0
    def __init__(self,marca,tipo_entrada):
        Teclado.contador_teclados += 1
        self._id_teclado=Teclado.contador_teclados
        #self._marca=marca
        #self._tipo_entrada=tipo_entrada
        #otra manera de iniciar los atributos es llamar al contructor de la clase padre es mas recomendado
        super().__init__(marca,tipo_entrada)
    def __str__(self):
        return f'Id: {self._id_teclado} ,Marca: {self._marca.upper()} , Tipo de entrada: {self._tipo_entrada.upper()}'

#codigo principal
if __name__ == '__main__':
    teclado1= Teclado('vorago','USB')
    print(teclado1)
    teclado2= Teclado('gamecraft','bluetooth')
    print(teclado2)