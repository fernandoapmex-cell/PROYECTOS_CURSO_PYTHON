from app import db


class Persona(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nombre=db.Column(db.String(255))
    apellido=db.Column(db.String(2555))
    email=db.Column(db.String(255))

    def __str__(self):
        return f'Id:{self.id} Nombre:{self.nombre} Apellido:{self.apellido} Email:{self.email}'
