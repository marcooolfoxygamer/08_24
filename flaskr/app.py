from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    u = Usuario(nombre_usuario='Juan', contrasena='12345')
    a = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)
    c = Cancion(titulo='mi cancion', minutos=1, segundos=15, interprete="Juanito")

    u.albumes.append(a)
    a.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()

    print(Album.query.all())
    print(Album.query.all()[0].canciones)
    print(Cancion.query.all())

    db.session.delete(a)
    print(Album.query.all())
    print(Cancion.query.all())

    #print(Usuario.query.all())
    #print(Usuario.query.all()[0].albumes)
    #db.session.delete(u)

    #print(Usuario.query.all())
    #print(Album.query.all())



