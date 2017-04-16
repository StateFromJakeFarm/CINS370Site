import cx_Oracle

def connect(user, passwd, host, path):
	return cx_Oracle.connect(user + '/' + passwd + '@' + host + path)

def query(conHandle, queryString):
	cur = conHandle.cursor()
	cur.execute(queryString)

	return cur
