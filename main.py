from flask import Flask
import os

from funcs import *

app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def root():
	queryStr = """
		SELECT * FROM WCPLAYERS14
	"""

	outStr = ""

	creds = ('user101', 'pass101', '127.0.0.1', '') 
	allRows = query(creds, queryStr)

	return makeTable((1,2,3,4,5,6,7,8,9,10,11,12,13), "border: 1px solid black", allRows)


if __name__ == '__main__':
    app.run()
