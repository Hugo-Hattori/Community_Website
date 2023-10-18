from flask import Flask, render_template, url_for, request, flash, redirect
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

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form: #verifica se o form é válido e qual botão foi clicado
        # exibir mensagem de login bem sucedido
        flash(f'Login bem sucedido no e-mail: {form_login.email.data}', 'alert-success')
        # redirecionar para a homepage
        return redirect(url_for('home'))

    if form_criarconta.validate_on_submit() and 'botao_submit_crianconta' in request.form: #verifica se o form é válido e qual botão foi clicado
        # criou conta com sucesso
        flash(f'Login bem sucedido no e-mail: {form_criarconta.email.data}', 'alert-success')
        # redirecionar para a homepage
        return redirect(url_for('home'))

    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)