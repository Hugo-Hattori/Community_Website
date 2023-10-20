from main import app, database
from models import Usuario, Post


# with app.app_context():
#     database.create_all()


# with app.app_context():
#     usuario = Usuario(username='Hugo', email='hugo@gmail.com', senha='123456')
#     usuario2 = Usuario(username='Renan', email='renan@gmail.com', senha='123456')
#
#     database.session.add(usuario)
#     database.session.add(usuario2)
#
#     database.session.commit()


# with app.app_context():
#     meus_usuarios = Usuario.query.all()
#     print(meus_usuarios)
#     primeiro_usuario = Usuario.query.first()
#     print(primeiro_usuario)
#     print(primeiro_usuario.username)
#     print(primeiro_usuario.id)
#     print(primeiro_usuario.email)


# with app.app_context():
#     usuario_teste = Usuario.query.filter_by(id=2).first()
#     print(usuario_teste.email)
#     usuario_teste = Usuario.query.filter_by(email='hugo@gmail.com').first()
#     print(usuario_teste.username)


# with app.app_context():
#     post_teste = Post(id_usuario=1, titulo='Meu primeiro post de teste', corpo='Hugo voando!')
#     database.session.add(post_teste)
#     database.session.commit()

# with app.app_context():
#     post = Post.query.first()
#     print(post)
#     print(post.titulo)
#     print(post.autor.email)


#When tests on database are over, execute the code below
with app.app_context():
    database.drop_all()
    database.create_all()