def sumar(a:int,b:int):
    resultado_suma=a+b
    return resultado_suma

#__name__ es para ver el main y la prueba solo se ejecute en el modulo
if __name__=='__main__':
    #prueba funcion sumar desde modulo
    print(sumar(15,67))