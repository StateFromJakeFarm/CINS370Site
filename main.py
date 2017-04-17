from flask import Flask
import os

from funcs import *

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET'])
def root():
    queryStr = """
        SELECT * FROM WC2014
    """

    outStr = ""

    creds = ('user101', 'pass101', '127.0.0.1', '') 
    allRows = query(creds, queryStr)

    colNames = ('Num','Name','Country','Club','League','Goals','Points')
    styling = 'border: 5px solid black'
    return makeTable(colNames, allRows, styling)

@app.route('/other', methods=['GET'])
def other():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run('0.0.0.0')
