from flask import Flask, request, render_template
from wtforms import Form, BooleanField, TextField, validators
import os

from funcs import *

app = Flask(__name__, static_url_path='')

class QueryForm(Form):
    query = TextField('Query', [validators.Required()])

@app.route('/query', methods=['GET', 'POST'])
def anyQuery():
    form = QueryForm()
    if request.method == 'POST':
        return request.form['query']

    return render_template('query.html', form=form)


if __name__ == '__main__':
    app.run('0.0.0.0')
