from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = 'db2c69f4682f60645d82121f462f9313'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'


database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #redirecionado páginas que requerem login para a página da função login
login_manager.login_message = 'Faça login para continuar.'
login_manager.login_message_category = 'alert-info'


from comunidade_impressionadora import models #isto é ncessário para criar as tabelas para o deploy
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table('usuario'):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('Base de Dados criada.')
else:
    print('Base de Dados já existente.')


from comunidade_impressionadora import routes