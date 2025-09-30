#revisar si una variable se encuentra dentro de rango entre 1 y 10

dato=int(input('proporciona un dato entero: '))

#Revisamos si esta en raango

esta_dentro_rango=1<=dato<=10
print(f'variable esta dentro del rango :{esta_dentro_rango}')

#revisamos la logica inversa si el dato esta fuera de rango
esta_dentro_rango =not( 1<= dato <= 10 )
print(f'variable esta fuera del rango :{esta_dentro_rango}')
