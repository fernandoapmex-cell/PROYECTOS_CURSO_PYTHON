print('Potencia de un numero pero unsando funcioens recursivas')

def potencia(base, exponente):
    #caso base
    if exponente == 0:
        return 1
    else: #caso recursivo
        return base * potencia(base, exponente -1)

print(potencia(2,3))