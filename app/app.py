from os import path

import markdown
from flask import Flask, render_template, Markup


app = Flask(__name__)


def render(f_name):
    with open(path.join('..', f_name)) as f:
        content = Markup(markdown.markdown(''.join(f.readlines())))
    return render_template('index.html', content=content)


@app.route('/')
def index():
    return render('should-I-cite-this-software.md')


@app.route('/how')
def how():
    return render('how-to-cite-software.md')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
