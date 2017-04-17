from flask import Flask, request, render_template
from wtforms import Form, BooleanField, TextField, validators
import os

from funcs import *

# DB login credentials, host, and path
creds = ('user101','pass101','127.0.0.1','/')

app = Flask(__name__, static_url_path='')

class QueryForm(Form):
    query = TextField('Query', [validators.Required()])

@app.route('/query', methods=['GET', 'POST'])
def query():
    # DB login credentials, host, and path
    creds = ('user101','pass101','127.0.0.1','/')

    # Form to hold our query
    form = QueryForm()

    # If we get a POST request (the query), display output in table
    if request.method == 'POST':
        queryStr = request.form['query']
        dataRows = query(creds, queryStr)
        return makeTable("", dataRows)

    # Else, display our template
    return render_template('query.html', form=form)

@app.route('/tables', methods=['GET', 'POST'])
def tables():
    return ""

if __name__ == '__main__':
    app.run('0.0.0.0')
