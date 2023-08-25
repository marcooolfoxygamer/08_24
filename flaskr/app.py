from flaskr import create_app
from .modelos import db, Cancion, Album, Usuario, Medio
from .modelos import AlbumSchema, CancionSchema, UsuarioSchema
from flask_restful import Api
from .vistas import VistaCanciones, VistaCancion, VistaAlbumes, VistaAlbum, VistaUsuarios, VistaUsuario

app = create_app("default")
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

api = Api(app)
api.add_resource(VistaCanciones,'/canciones')
api.add_resource(VistaCancion,'/canciones/<int:id_cancion>')
api.add_resource(VistaAlbumes,'/albums')
api.add_resource(VistaAlbum,'/albums/<int:id_album>')
api.add_resource(VistaUsuarios,'/usuarios')
api.add_resource(VistaUsuario,'/usuarios/<int:id_usuario>')

with app.app_context():
    # Usuario
    Usuario_Schema = UsuarioSchema()
    U = Usuario(nombre_usuario='Juan', contrasena='12345')

    # Album
    Album_Schema = AlbumSchema()
    A = Album(titulo='prueba', anio=1999, descripcion='texto', medio=Medio.CD)

    # Cancion
    Cancion_Schema = CancionSchema()
    C = Cancion(titulo='mi cancion', minutos=1, segundos=15, interprete="Juanito")

    U.albumes.append(A)
    A.canciones.append(C)

    db.session.add(U)
    db.session.add(C)
    #db.session.add(A)
    db.session.commit()

    print([Album_Schema.dumps(album) for album in Album.query.all()])
    print([Cancion_Schema.dumps(cancion) for cancion in Cancion.query.all()])
    print([Usuario_Schema.dumps(usuario) for usuario in Usuario.query.all()])



    """
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
    """


