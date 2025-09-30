class Aritmetica:
        def __init__(self, operando1=None,operando2=None):
            self.operando1 = operando1
            self.operando2 = operando2

        def sumar(self):
            resultado =  self.operando1 + self.operando2
            return resultado

        def resta(self):
            resultado = self.operando1 - self.operando2
            return resultado

        def multiplicar(self):
            resultado = self.operando1 * self.operando2
            return resultado

        def dividir(self):
            resultado = self.operando1 / self.operando2
            return resultado

#programa principal
if __name__ == '__main__':
    print('Ejemplo clase aritmetica')
    aritmetica1 = Aritmetica(5,7)
    print('El resultado de dividir: ',aritmetica1.dividir())
    print('El resultado de multiplicar: ',aritmetica1.multiplicar())
    print('El resultado de sumar: ',aritmetica1.sumar())
    print('El resultado de resta: ',aritmetica1.resta())
    #segundo objeto
    aritmetica2 = Aritmetica(12,16)
    aritmetica2.sumar()
    print('El resultado de dividir: ',aritmetica2.dividir())
    print('El resultado de multiplicar: ',aritmetica2.multiplicar())
    print('El resultado de sumar: ',aritmetica2.sumar())
    print('El resultado de resta: ',aritmetica2.resta())
    aritmetica3 = Aritmetica(7)
    aritmetica3.operando2 = 3
    print('El resultado de sumar: ',aritmetica3.sumar())