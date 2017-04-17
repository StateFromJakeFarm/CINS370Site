from flask import Flask, request, render_template
from wtforms import Form, BooleanField, TextField, validators
import os

from funcs import *
from forms import *

# DB login credentials, host, and path
creds = ('user101','pass101','127.0.0.1','/')

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def root():
    return render_template('index.html')

@app.route('/query', methods=['GET', 'POST'])
def userQuery():
    # Form to hold our query
    form = QueryForm()

    # Display our template
    retStr = render_template('query.html', form=form)

    # If we get a POST request (the query), display output in table
    if request.method == 'POST':
        queryStr = request.form['query']
        dataRows = query(creds, queryStr)
        return retStr + makeTable("", dataRows)

    return retStr

@app.route('/tables', methods=['GET', 'POST'])
def tables():
    fname = ""
    if request.method == 'POST':
        myQuery = ""
        sel = request.form['querySel']
        if sel == "Earnings":
            myQuery = getQueryFromFile('earnings.sql')

        fname = randFName() + '.jpg'
        rows = query(creds, myQuery)
        barGraph(rows, fname, 'Club', 'Earnings (mil Euros)')

    return render_template('tables.html', filename=fname)

    # Delete the file after it is served
    @app.after_request
    def delImg(response):
        serverDel(fname)
        return response


if __name__ == '__main__':
    app.run('0.0.0.0')
