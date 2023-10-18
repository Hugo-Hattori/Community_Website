from flask import Flask, render_template, url_for
from forms import FormLogin, FormCriarConta


lista_usuarios = ['Hugo', 'Alexandre', 'Renan', 'Amanda']


app = Flask(__name__)
app.config['SECRET_KEY'] = 'db2c69f4682f60645d82121f462f9313'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/lista-usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)