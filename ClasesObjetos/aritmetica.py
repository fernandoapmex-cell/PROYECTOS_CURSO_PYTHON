class Aritmetica:
        def __init__(self, operando1=None,operando2=None):
            self._operando1 = operando1
            self._operando2 = operando2

        def sumar(self):
            resultado =  self._operando1 + self._operando2
            return resultado

        def resta(self):
            resultado = self._operando1 - self._operando2
            return resultado

        def multiplicar(self):
            resultado = self._operando1 * self._operando2
            return resultado

        def dividir(self):
            resultado = self._operando1 / self._operando2
            return resultado

        @property
        def operando1(self):
            return self._operando1

        @operando1.setter
        def operando1(self, operando1):
            self._operando1 = operando1

        @property
        def operando2(self):
            return self._operando2

        @operando2.setter
        def operando2(self, operando2):
            self._operando2 = operando2

#programa principal
if __name__ == '__main__':
    print('Ejemplo clase aritmetica')
    aritmetica1 = Aritmetica(5,7)
    print(f'Valor operando1 del objeto artitmetica 1: {aritmetica1.operando1}')
    print(f'Valor operando1 del objeto artitmetica 1: {aritmetica1.operando2}')
    print('El resultado de dividir: ',aritmetica1.dividir())
    print('El resultado de multiplicar: ',aritmetica1.multiplicar())
    print('El resultado de sumar: ',aritmetica1.sumar())
    print('El resultado de resta: ',aritmetica1.resta())
    #segundo objeto
    aritmetica2 = Aritmetica(12,16)
    print(f'Valor operando1 del objeto artitmetica 2: {aritmetica2.operando1}')
    print(f'Valor operando1 del objeto artitmetica 2: {aritmetica2.operando2}')
    aritmetica2.sumar()
    print('El resultado de dividir: ',aritmetica2.dividir())
    print('El resultado de multiplicar: ',aritmetica2.multiplicar())
    print('El resultado de sumar: ',aritmetica2.sumar())
    print('El resultado de resta: ',aritmetica2.resta())
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 3
    print('El resultado de sumar: ',aritmetica3.sumar())