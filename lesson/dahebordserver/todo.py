from flask import Flask

app = Flask(__name__)

@app.route('/')
def index_page():
    return '<p>Index Page</p>'

@app.route('/hello')
def hello():
    return 'helloo!!'


@app.route('/eroor')
def raise_eroor():
    raise RuntimeError('eror')

@app.route('/hello/<name>')
def hello_user(name):
    return f'Hello {name.capitalize()}!!!'