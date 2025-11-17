#Metodos de instancia de clase y estatic y sus diferencias
class MiClase:
    def metodo_instancia(self):
        #retornamos una tupla
        return 'Metodo de instancia ejecutado..',self
    @classmethod
    def metodo_clase(cls):
        #retornamos una tupla
        return 'Metodo de clase ejecutado..',cls
    @staticmethod
    def metodo_estatico():
        #estos metodos no pueden obtener informacion de la clase u objeto
        return 'Metodo estatico ejecutado..'
#Caso 1.- instancia implicita
objeto = MiClase()
print(objeto.metodo_instancia())
#Caso 2. Instancia explicita
print(MiClase.metodo_instancia(objeto))
#Caso 3.- Eecutamos el metodo de insntacia desde la clase
#print(MiClase.metodo_instancia(MiClase)) - No es posible pq necesita un objeto
#Caso 4.- Ejeutamos el metodo de clase
print(MiClase.metodo_clase())
#Caso 5 Desde las instancias podemos acceder a los metodos de calse
print(objeto.metodo_clase())
#caso estatico para llamar el metodo estatico
print(MiClase.metodo_estatico())
#caso 7 lo ejecutamos desde la instancia
print(objeto.metodo_estatico())