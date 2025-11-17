#crear unaclase para definir expcepciones personalizadas
#Ej.Validar que un nombre no pueda tener menos de 3 caracteres
#este tipo de validacion no indica cual es el problema en especifico

def validar(nombre_completo):
    if len(nombre_completo)<3:
        raise ValueError
    else:
        return print('Validacion Correcta....')



#validacion personalizda,indica cual es el problema y queda auto documentado
# class NombreCorto(ValueError):
#     pass
#
# def Validar_Mejorado(nombre_completo):
#     if len(nombre_completo) < 3:
#         raise NombreCorto(nombre_completo)
#     else:
#         return print('Validacion Correcta....')
# nombre = 'f'
# Validar_Mejorado(nombre)

#es buena idea crear una clase base y de alli extender a las demas clases

class ClaseExcepcionBase(TypeError):
    pass

class NombreCortoMejorado(ClaseExcepcionBase):
    pass
def Validar_Mejorado(nombre_completo):
    if len(nombre_completo) < 3:
        raise NombreCortoMejorado(nombre_completo)
    else:
        return print('Validacion Correcta....')
try:
    nombre = 'f'
    Validar_Mejorado(nombre)
except ClaseExcepcionBase as e:
    print(f'{type(e).__name__},Linea de error:{e.__traceback__.tb_lineno} en el archivo: {__file__}: {e}')