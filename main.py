from flask import Flask
import os

from funcs import *

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def root():
	conHandle = connect('user101', 'pass101', '127.0.0.1', '')
	queryStr = """
		SELECT * FROM WCPLAYERS14
	"""

	outStr = ""

	allRows = query(conHandle, queryStr)
	for row in allRows:
		outStr += str(row)
		outStr += '<br>'

	return outStr

if __name__ == '__main__':
    app.run()
