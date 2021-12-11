# Створити hmtm-сторінку "create_greeting" з можливістю залишення новорічних привітань.
# На сторінці повинно вводиди "namе", "text", "url картинки".
# Після натискання на кнопку "save" створюється привітання з текстом:
# "Dear {name}! {text}" і нижче відображаєтька картинка по введеному {url картинки}.
# На сторінці такою є кнопка "All greetings", яка перенаправляє  на сторінку "all_greetings".
# Cторінка "all_greetings" відображає всі створені раніше привітання.
# Всі коли-небудь створені привітання записуються в json-файл.
# Після перезапуску серверу всі раніше створені привітання виводяться на сторінку "all_greetings".

from flask import Flask, render_template, request

from model import Greeting

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        text = request.form['text']
        url = request.form['url']
        new_greeting = Greeting(name, text, url)
        new_greeting.load_image()
        srt_greeting = f'Dear {new_greeting.name}! \n {new_greeting.text}'
        return render_template('base.html', name_greeting=f'Dear {new_greeting.name}!', name_text=f'{new_greeting.text}',
                               file_name=new_greeting.url)
    return render_template('base.html')


@app.route('/all_greetings')
def all_greetings():
    return render_template('all_greetings', greetings=Greeting.all_greeting)


