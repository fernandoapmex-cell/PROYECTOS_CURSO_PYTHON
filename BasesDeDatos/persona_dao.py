from conexion import Conexion
from cursor_pool import CursorPool
from persona import Persona
from logger_base import log

class PersonaDAO:
    '''
    DAO (Data Access Object)
    CRUD (Create - Read -Update -Delete)


    '''

    _SELECCIONAR='SELECT * FROM persona ORDER BY id_persona'
    _INSERTAR='INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
    _ACTUALIZAR='UPDATE persona SET nombre=%s,apellido=%s,email=%s WHERE id_persona=%s'
    _ELIMINAR='DELETE FROM persona WHERE id_persona=%s'

    @classmethod
    def seleccionar(cls):
    #usaremos un with para cerrar la conexion
        with CursorPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            personas=[]
            for registro in registros:
                #aca creamos el objeto de tipo persona para crear el objeto con los datos de la bd
                persona = Persona(registro[0],registro[1],registro[2],registro[3])
                personas.append(persona)
            return personas

    @classmethod
    def insertar(cls, persona):
        with CursorPool() as cursor:
            valores=(persona.nombre,persona.apellido,persona.email)
            cursor.execute(cls._INSERTAR,valores)
            log.debug(f'Persona insertada: {persona}')
            return cursor.rowcount

    @classmethod
    def actualizar(cls, persona):
        with CursorPool() as cursor:
            valores= (persona.nombre,persona.apellido,persona.email,persona.id_persona)
            cursor.execute(cls._ACTUALIZAR,valores)
            log.debug(f'Persona actualizada: {persona}')
            return cursor.rowcount
    @classmethod
    def eliminar(cls, persona):
        with CursorPool() as cursor:
            valores=(persona.id_persona,)
            cursor.execute(cls._ELIMINAR,valores)
            log.debug(f'Persona eliminada: {persona}')
            return cursor.rowcount

if __name__ == '__main__':
    #insertar un registro
    # persona1 = Persona(nombre='Pedro',apellido='najera',email='pnajera@mail.com')
    # personas_insertadas=PersonaDAO.insertar(persona1)
    # log.debug(f'Personas insertadas: {personas_insertadas}')

    #actualizar un registro
    # persona1 =Persona(27,'chalin rivers','Juarez','rivers@mail.com')
    # personas_actualizadas=PersonaDAO.actualizar(persona1)
    # log.debug(f'Personas Actualizadas: {personas_actualizadas}')

    #eliminar un registro
    # persona1 = Persona(id_persona=27)
    # personas_eliminadas=PersonaDAO.eliminar(persona1)
    # log.debug(f'Personas eliminadas: {personas_eliminadas}')
    #seleccionar objetos
    personas = PersonaDAO.seleccionar()
    for persona in personas:
        log.debug(persona)