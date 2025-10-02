from ClasesObjetos.sistema_empleados.empleado import Empleado
from ClasesObjetos.sistema_empleados.empresa import Empresa

print('***Sistema empleados ***')

#creacion de una instancia de empresa

empresa1 = Empresa('Carnitas Chalo')

#contratar empleados

empresa1.contratar_empleado('Juan','Ventas')
empresa1.contratar_empleado('Chabelo','Marketing')
empresa1.contratar_empleado('Garnacho','Ventas')
empresa1.contratar_empleado('Daniel','Oficina')

#obtener total objetos de tipo empleado

print(f'Total de empleados :',Empleado.obtener_total_empleados())

#obtener el numero de empleados en el departamento de ventas

print(f'''
    Empleados en el departamento de ventas:
    {empresa1.obtener_empleados_por_departamento('Ventas')}
''')

#total empleados de la empresa
empresa1.obtener_total_empleados_empresa()


empresa2 = Empresa('Carnicos Ramirez')
empresa2.contratar_empleado('Juan','Ventas')
empresa2.contratar_empleado('Chabelo','Marketing')
empresa2.contratar_empleado('Garnacho','Ventas')
empresa2.contratar_empleado('Daniel','Oficina')
empresa2.contratar_empleado('Juan','Carniboros')
empresa2.contratar_empleado('Chabelo','Viene Viene')
empresa2.contratar_empleado('Garnacho','Carnicero')
empresa2.contratar_empleado('Daniel','Oficina')

#ambas empresas
print(f'Total de empleados :',Empleado.obtener_total_empleados())

#total empleados de la empresa
empresa2.obtener_total_empleados_empresa()