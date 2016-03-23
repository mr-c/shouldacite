from os import path

import markdown
from flask import Flask, render_template, Markup


app = Flask(__name__)


@app.route('/')
def index():
    with open(path.join('..', 'decision-tree.md')) as f:
        content = Markup(markdown.markdown(''.join(f.readlines())))
    return render_template('index.html', content=content)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
