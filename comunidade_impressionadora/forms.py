from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from comunidade_impressionadora.models import Usuario


class FormCriarConta(FlaskForm):
    username = StringField('Nome de Usuário', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    confirmacao_senha = PasswordField('Confirme a Senha', validators=[DataRequired(), EqualTo('senha')])
    botao_submit_crianconta = SubmitField('Criar Conta')

    # temos que usar exatamente este nome na função pois essa é uma funcionalidade do validate_on_submit do flask
    def validate_email(self, email):
        usuario = Usuario.query.filter_by(email=email.data).first()
        if usuario:
            #obs: tive que colocar a mensagem de erro em inglês devido ao Translate que estou utilizando
            raise ValidationError('E-mail address already registered. Sign up with another e-mail address or log in to continue.')


class FormLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    senha = PasswordField('Senha', validators=[DataRequired(), Length(6, 20)])
    lembrar_logado = BooleanField('Me manter logado?')
    botao_submit_login = SubmitField('Fazer Login')