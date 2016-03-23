from os import path
from collections import OrderedDict

import markdown
from flask import Flask, render_template, Markup


app = Flask(__name__)


def render(f_name, what=None):
    with open(path.join('..', f_name)) as f:
        content = Markup(markdown.markdown(''.join(f.readlines())))
    return render_template('index.html', content=content, what=what)


@app.route('/')
@app.route('/<what>')
def index(what=''):
    pages = OrderedDict(
        [
            ('', ('should-I-cite-this-software.md', 'Should I?')),
            # ('how.html', ('how_make_citable.html', 'How to cite?')),
            ('how.html', ('how-to-cite-software.md', 'How to cite?')),
            ('example1.html', ('SampleWorkflow.md', 'Example 1')),
            ('example2.html', ('SampleWorkflowNoCitation.md', 'Example 2')),
        ]
    )
    f_name, caption = pages[what]

    with open(path.join('..', f_name)) as f:
        content = Markup(markdown.markdown(''.join(f.readlines())))

    return render_template('index.html', content=content, what=what, pages=pages)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
