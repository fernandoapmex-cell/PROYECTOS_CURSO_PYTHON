from ClasesObjetos.mundo_pc.dispositivo_entrada import DispositivoEntrada


class Raton(DispositivoEntrada):
    contador_ratones = 0
    def __init__(self,marca,tipo_entrada):
        Raton.contador_ratones += 1
        self._id_raton=Raton.contador_ratones
        #self._marca=marca
        #self._tipo_entrada=tipo_entrada
        #otra manera de iniciar los atributos es llamar al contructor de la clase padre es mas recomendado
        super().__init__(marca,tipo_entrada)
    def __str__(self):
        return f'Id: {self._id_raton} ,Marca: {self._marca.upper()} , Tipo de entrada: {self._tipo_entrada.upper()}'

#codigo principal
if __name__ == '__main__':
    raton1= Raton('hp','USB')
    print(raton1)
    raton2= Raton('acer','bluetooth')
    print(raton2)