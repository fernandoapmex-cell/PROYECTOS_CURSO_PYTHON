#profundizar en set
#es una coleccion de elementos unicos y es mutable
#los elementos de un set son inmutables
conjunto={'Juan',True,18.0}
print(conjunto)
#set vacio
#asi no por que seria un diccionario vario
conjunto={}
print(type(conjunto))
#set vacio
conjunto=set()
print(conjunto)
print(type(conjunto))
#agregar valores a set
conjunto.add('Juan')
#contiene valores unicos
conjunto.add('Juan')
#no se pueden agregar 2 veces el mismo valor al set
print(conjunto)
#crear un set apartir de un iterable
conjunto=set([4,6,8,32,7,9,45,3,4,4])
print(conjunto)
#podemos agregar mas elementos
conjunto2={100,200,300,400,300}
conjunto.update(conjunto2)
print(conjunto)
conjunto.update([40,30,20,20,100])
print(conjunto)

#copiar un set (copia poco profunda)
conjunto_copia=conjunto.copy()
print(conjunto_copia)
#verificar la igualdad de los 2 sets de contenido y referencia
print(f'Es iguual en contenido',conjunto_copia == conjunto)
print(f'Es la misma referencia?',conjunto_copia is conjunto)

#operaciones de conjuntos utilizando sets
#personas con distintas caracteristicas

pelo_negro={'juan','karla','pedro','maria'}
pelo_rubio={'lorenzo','laura','marco'}
ojos_cafe={'karla','laura'}
menores_30={'juan','karla','maria'}
#Todos los elementos con ojo color cafe y pelo rubio(union) no se repiten los elementos
print(ojos_cafe.union(pelo_rubio))
#invertir el orden con el mismo resultado (conmutativa)
print(pelo_rubio.union(ojos_cafe))
#interseccion Solo las personas con ojop color cafe y pelo rubio tambien es conmutativa
print(ojos_cafe.intersection(pelo_rubio))
#(diference)pelo negro sin ojos color cafe , esta no es conmutativa
print(pelo_negro.difference(ojos_cafe))
#diferencia simetrica pelo negro u ojos cafe pero no ambos esta si es conmutativa
print(pelo_negro.symmetric_difference(ojos_cafe))

#preguntar si un set esta contenido en otro un subset
#revisamos si los elementos del primer set estan contenidos en el segundo set
print(menores_30.issubset(pelo_negro))
#preguntar si un set contiene a otro set
#revisar si los elementos del primer set estan contenidos en el segudno set
print(menores_30.issuperset(pelo_negro))
#preguntar si los de pelo negro no tienen pelo rubio(disjoin)
print(pelo_negro.isdisjoint(pelo_rubio))