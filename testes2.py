from comunidade_impressionadora import database, app
from comunidade_impressionadora.models import Usuario


with app.app_context():
    #criando novo banco de dados
    # database.drop_all()
    # database.create_all()

    #testando se o usuário foi criado
    print(Usuario.query.all())
    usuario = Usuario.query.first()
    print(usuario.email)
    print(usuario.senha)
    print(usuario.username)