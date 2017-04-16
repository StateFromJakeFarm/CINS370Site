import cx_Oracle

def connect(user, passwd, host, path):
	"""Get connection handle for DB"""
	return cx_Oracle.connect(user + '/' + passwd + '@' + host + path)

def query(creds, queryString):
	"""Retrieve output of query as list of lists"""
	conHandle = connect(*creds)
	cur = conHandle.cursor()
	cur.execute(queryString)

	rows = []
	for row in cur:
		rows.append(list(row))

	conHandle.close()

	return rows

def makeTable(colNames, styling, rows):
	"""Create a simple html table based on DB output"""
	retStr = "<table"

	if styling != "":
		retStr += " style=\"" + styling + "\""

	retStr += "> <tr>"

	# Add column names as 1st row
	for colName in colNames:
		item = "<th>" + str(colName) + "</th>"
		retStr += item
	retStr += "</tr>"

	# Add all rows
	for row in rows:
		retStr += "<tr>"
		for value in row:
			item = "<td>" + str(value) + "</td>"
			retStr += item
		retStr += "</tr>"

	return retStr + "</table>"
