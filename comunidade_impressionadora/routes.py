from comunidade_impressionadora import app, database, bcrypt
from flask import render_template, redirect, url_for, flash, request
from comunidade_impressionadora.forms import FormLogin, FormCriarConta, FormEditarPerfil
from translate import Translator
from comunidade_impressionadora.models import Usuario
from flask_login import login_user, logout_user, current_user, login_required
from PIL import Image
import secrets
import os
from wtforms import BooleanField


lista_usuarios = ['Hugo', 'Alexandre', 'Renan', 'Amanda']


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/lista-usuarios')
@login_required
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
            para_next = request.args.get('next')
            if para_next:
                return redirect(para_next) #redireciona para a página que queria entrar antes do login
            else:
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


@app.route('/sair')
@login_required
def logout():
    logout_user()
    flash('Logout feito com sucesso!', 'alert-success')
    return redirect(url_for('home'))


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)


@app.route('/post/criar')
@login_required
def criar_post():
    return render_template('criarpost.html')


def salvar_imagem(imagem):
    # mudar o nome do arquivo da imagem antes de salvá-lo (utilizando um código aleatório)
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    novo_nome_arquivo = nome + codigo + extensao

    # compactar a imagem
    tamanho = (200, 200)
    imagem_compactada = Image.open(imagem)
    imagem_compactada.thumbnail(tamanho)

    # salvar a imagem na pasta fotos_perfil
    caminho_completo = os.path.join(app.root_path, 'static/fotos_perfil', novo_nome_arquivo)
    imagem_compactada.save(caminho_completo)
    return novo_nome_arquivo


def atualizar_cursos(form):
    lista_cursos = []
    for campo in form:
        if 'curso_' in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    lista_cursos = ';'.join(lista_cursos)  # transformando a lista uma única string
    if len(lista_cursos) == 0:
        lista_cursos = 'Não Informado'
    return lista_cursos


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    traduzir = Translator(from_lang="English", to_lang="Portuguese")

    form = FormEditarPerfil()
    if form.validate_on_submit(): #neste caso estamos fazendo um request do tipo POST ao apertar o botão de submit
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            # mudar o campo foto_perfil para o nome da nova imagem
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.cursos = atualizar_cursos(form)
        database.session.commit()
        flash(f'Perfil atualizado com sucesso!', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET': #o método request do tipo GET acontece automaticamente qdo a página é carregada
        form.email.data = current_user.email
        form.username.data = current_user.username
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form, traduzir=traduzir)