nombre_completo=' Ubaldo Acosta Soto '
nombre_empresa=' Global Mentoring '
dominio='.com.mx'
print(f'nombre del usuario: {nombre_completo}')
nombre_usuario = nombre_completo.strip()
nombre_usuario=nombre_usuario.replace(' ','.')
nombre_usuario=nombre_usuario.lower()
print(f'nombre de usuario normalizado {nombre_usuario}')
print(f'nombre empresa: {nombre_empresa}')
print(f'nombre de dominio {dominio}')
nombre_empresa_normalizado=nombre_empresa.replace(' ','').lower()
print(f'nombre de empresa normalizado {nombre_empresa_normalizado}')
dominio_email=f'@{nombre_empresa_normalizado}{dominio}'
print(dominio_email)
email_final=f'{nombre_usuario}{nombre_empresa_normalizado}{dominio_email}'
print(email_final)