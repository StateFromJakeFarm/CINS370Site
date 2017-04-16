import cx_Oracle

def connect(user, passwd, host, path):
	return cx_Oracle.connect(user + '/' + passwd + '@' + host + path)

def query(creds, queryString):
	conHandle = connect(*creds)
	cur = conHandle.cursor()
	cur.execute(queryString)

	rows = []
	for row in cur:
		rows.append(row)

	conHandle.close()

	return rows
