#profundizando tipo float
a=3.0
print(f'a={a:.2f}')
#contructor de tipo flotante puede recibir int o string
a=float(10)
a=float('20')
print(f'a={a:.2f}')
#notacion exponencial
a=3e5
a=3e-5
print(f'a={a:.10f}')
#cualquier calculo que use un float se pasa a float
a=4.0+5
print(f'a={a}')
print(type(a))