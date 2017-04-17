from flask import Flask, request, render_template
from wtforms import Form, BooleanField, TextField, validators
import os

from funcs import *
from forms import *

# DB login credentials, host, and path
creds = ('user101','pass101','127.0.0.1','/')

app = Flask(__name__, static_url_path='')

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
    numQuery = """
        SELECT Num FROM PLAYERS
    """
    rows = query(creds, numQuery)
    return barGraph(rows, 'temp.png')

#    return render_template('viewImage.html', filename='ourGreatLeader.jpg')


if __name__ == '__main__':
    app.run('0.0.0.0')
