from comunidade_impressionadora import database, app
from comunidade_impressionadora.models import Usuario, Post
from flask_bcrypt import Bcrypt

with app.app_context():
    # #criando novo banco de dados
    # database.drop_all()
    # database.create_all()

    # #testando se o usuário foi criado
    # print(Usuario.query.all())
    # usuario = Usuario.query.first()
    # print(usuario.email)
    # print(usuario.senha)
    # print(usuario.username)
    #
    # #testando a criptografia da senha
    # usuario2 = Usuario.query.filter_by(username='novohugo').first()
    # print(usuario2)
    # print(usuario2.senha)
    #
    # #criando uma senha teste e verificando a criptografia
    # bcrypt = Bcrypt()
    # password = '123456'
    # pass_crypt = bcrypt.generate_password_hash(password)
    # print(bcrypt.check_password_hash(pass_crypt, '123456'))
    # print(bcrypt.check_password_hash(pass_crypt, 'this_is_not_the_password'))

    # #testando edição de cursos que o usuário possui
    # usuario = Usuario.query.filter_by(email='hugoteste@hotmail.com').first()
    # print(usuario.cursos)

    #testando a criação de post no banco de dados
    post = Post.query.first()
    print(post)
    print(post.titulo)
    print(post.corpo)
    print(post.autor)
    print(post.id_usuario)