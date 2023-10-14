from flask import Flask

app = Flask(__name__)


@app.route('/') #o decorator atribui uma funcionalidade a função abaixo dele
def home():
    return '<h1> Site no ar!! </h1>' \
           '<p> Esse site ta ficando legal! <p>'

@app.route('/contato')
def contato():
    return '<h2>Qualquer mande um e-mail para listavip@hashtagtreinamentos.com </h2>'


if __name__ == '__main__':
    app.run(debug=True)