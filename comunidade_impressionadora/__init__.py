from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
app.config['SECRET_KEY'] = 'db2c69f4682f60645d82121f462f9313'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login' #redirecionado páginas que requerem login para a página da função login
login_manager.login_message = 'Faça login para continuar.'
login_manager.login_message_category = 'alert-info'


from comunidade_impressionadora import routes