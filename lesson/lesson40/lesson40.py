from flask import Flask, render_template, redirect, request, session, url_for


app = Flask(__name__)
app.secret_key = 'qwertyui'

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        session['login'] = login
        session['password'] = password
        return redirect(url_for('autoriz'))
    return render_template('register.html')


@app.route('/autoriz', methods=['GET', 'POST'])
def autoriz():
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        if login == session['login'] and password == session['password']:
            return redirect(url_for('index'))
    return render_template('autoriz.html')

@app.route('/index')
def index():
    if 'login' in session:
        return render_template('index.html', greeting=f'Greeting {session["login"]}!')
    return 'You are not logged in'

@app.route('/logout')
def logout_user():
    session.pop('log', None)
    session.pop('password', None)
    return redirect(url_for('autoriz'))