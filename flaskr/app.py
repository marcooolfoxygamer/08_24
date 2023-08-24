from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    c = Cancion(titulo='Prueba', minutos=2, segundos=25, interprete="Juanito")
    db.session.add(c)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():

    a = Album(titulo='Alb_Prueba', anio=2012, descripcion='album de ejemplo', medi='CD')
    db.session.add(a)
    db.session.commit()
    print(Cancion.query.all())

with app.app_context():
    u = Usuario(nombre_usuario='Pepito', contrasena='123')
    db.session.add(u)
    db.session.commit()
    print(Cancion.query.all())


