from comunidade_impressionadora import app, database, bcrypt
from flask import render_template, redirect, url_for, flash, request
from comunidade_impressionadora.forms import FormLogin, FormCriarConta
from translate import Translator
from comunidade_impressionadora.models import Usuario
from flask_login import login_user


lista_usuarios = ['Hugo', 'Alexandre', 'Renan', 'Amanda']


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
    traduzir = Translator(from_lang="English", to_lang="Portuguese")

    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form: #verifica se o form é válido e qual botão foi clicado
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_logado.data)
            flash(f'Login bem sucedido no e-mail: {form_login.email.data}', 'alert-success')
            return redirect(url_for('home'))
        else:
            flash('Falha no login. E-mail ou senha incorretos.', 'alert-danger')

    if form_criarconta.validate_on_submit() and 'botao_submit_crianconta' in request.form: #verifica se o form é válido e qual botão foi clicado
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuario(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Conta criada com sucesso para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta, traduzir=traduzir)