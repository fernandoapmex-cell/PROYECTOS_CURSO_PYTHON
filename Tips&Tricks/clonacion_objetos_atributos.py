#Copia de atributos de objetos
import copy


#definimos una clase de tipo punto 2D
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Punto ({self.x!r}, {self.y!r})'
    def __eq__(self, otro):
        #se pregunta si la variable recibida es de tipo Punto
        return isinstance(otro,Punto) and self.x == otro.x and self.y == otro.y

punto_a=Punto(1, 2)
punto_b= copy.copy(punto_a)
#copia poco profunda(shallow),son distintos objetos
print(f'copia poco profunda (shallow)')
print('Punto a:',punto_a)
print('Punto b:',punto_b)
print(f'Son objetos con el mismo contenido:{punto_a == punto_b}')
print(f'Son los mismos objetos (misma referencia):{punto_a is punto_b}')

#Clase rectangulo utiliza 2 puntos como referencia (superior izquierdo e inferior derecho)

class Rectangulo:
    def __init__(self, sup_izq, inf_der):
        self.sup_izq = sup_izq
        self.inf_der = inf_der
    def __repr__(self):
        return f'repr:Rectangulo({self.sup_izq!r}, {self.inf_der!r})'

rectangulo_a=Rectangulo(Punto(0,1), Punto(3,4))
print(rectangulo_a)
#copia superficial(shallow)
rectangulo_b=copy.copy(rectangulo_a)
print(f'Copia superficial rectangulos')
print(f'Rectangulo a: {rectangulo_a}')
print(f'Rectangulo b: {rectangulo_b}')
#debido a que la copia fue superficial,un cambio en un punto afecta al otro rectangulo
rectangulo_a.inf_der.y=6
print(f'Rectangulo cambio en un punto afecta al otro rectangulo a: {rectangulo_a}')
print(f'Rectangulo cambio al otro afexta al otro rectangulo b: {rectangulo_b}')

#creacion de una copia profunda

rectangulo_c=copy.deepcopy(rectangulo_a)
#modificamos el valor en un punto y esto no afecta al otro rectangulo
rectangulo_c.sup_izq.x = 2
print(f'Rectangulo cambio en un punto afecta al otro rectangulo a: {rectangulo_a}')
print(f'Rectangulo cambio al otro afexta al otro rectangulo b: {rectangulo_b}')
print(f'rectangulo c:{rectangulo_c}')

