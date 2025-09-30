print('***Sistema de Envios***')

#constantes
#definimos las tarifas de envio por kilo

TARIFA_NACIONAL = 10
TARIFA_INTERNACIONAL= 20

destino=input('Ingresa el destino del paquete(Nacional/Internacional): ').strip().lower()
peso=float(input('Ingresa el peso del paquete en kilogramos : '))

#calculo del envio del paquete

costo_envio = None

if destino == 'nacional':
    costo_envio=peso*TARIFA_NACIONAL
elif destino == 'internacional':
    costo_envio=peso*TARIFA_INTERNACIONAL
else:
    print('El destino ingresado no es valido ,ingresa valor nacional o internacional')

#Mostramos el costo de envio solo si es un valor valido

if costo_envio is not None:
    print(f'EL costo de envio del paquete es: ${costo_envio:.2f}')