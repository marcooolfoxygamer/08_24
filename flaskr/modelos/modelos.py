from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Medio(db.Model):
    med = db.Column(db.String(120), primary_key = True)
class Cancion(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    titulo = db.Column(db.String(120))
    minutos = db.Column(db.Integer)
    segundos = db.Column(db.Integer)
    interprete = db.Column(db.String(120))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo,self.minutos,self.segundos,self.interprete)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120))
    anio = db.Column(db.Integer)
    descripcion = db.Column(db.String(120))
    medi = db.Column(db.String(120))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.titulo,self.anio,self.descripcion,self.medi)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_usuario = db.Column(db.String(120))
    contrasena = db.Column(db.String(120))

    def __repr__(self):
        return "{}-{}-{}-{}".format(self.nombre_usuario,self.contrasena)

