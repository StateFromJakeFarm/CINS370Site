import cx_Oracle
import matplotlib.pyplot as plt
import numpy
import StringIO

from flask import make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

# DB #
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

def makeTable(colNames, rows, styling=None):
    """Create a simple html table based on DB output"""
    retStr = "<table"

    if styling is not None:
        retStr += " style=\"" + styling + "\""

    retStr += ">"

    # Add column names as 1st row
    retStr += "\n<tr>"
    if len(rows[0]) != 1:
        for colName in colNames:
            item = "<th>" + str(colName) + "</th>"
            retStr += item
    else:
        retStr += "<th>" + str(colNames) + "</th>"
    retStr += "</tr>"

    # Add all rows
    for row in rows:
        retStr += "\n<tr>"
        for value in row:
            item = "<td>" + str(value) + "</td>"
            retStr += item
        retStr += "</tr>"

    return retStr + "</table>"


# PLOTTING #
def barGraph(rows, fname, width=0.5):
    data = []
    for row in rows:
        val = row[0]
        if val is str or val is int:
            data.append(int(val))

    fig, ax = plt.subplots()
    inds = numpy.arange(len(data))
    rects = ax.bar(inds, data, width, color='b')

    canvas = FigureCanvas(fig)
    pngOut = StringIO.StringIO()
    canvas.print_png(pngOut)
    response = make_response(pngOut.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response

# GENERAL #
def serverSave(figObj, fname):
    figObj.savefig('static/' + fname)

def serverDel(fname):
    os.remove('/home/jakeh/school/databases/CINS370Site/static/' + fname)
