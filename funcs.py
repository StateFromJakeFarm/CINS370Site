import cx_Oracle
import matplotlib.pyplot as plt
import numpy
import os
import random
import string

from PIL import Image

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
def barGraph(rows, fname, xlab, ylab, width=0.5):
    data = []
    labels = []
    for row in rows:
        val = row[0]
        label = row[1]
        if val is not None and label is not None:
            data.append(int(val))
            labels.append(str(label))

    fig, ax = plt.subplots()
    inds = numpy.arange(len(data))
    rects = ax.bar(inds, data, width, color='b')
    plt.xticks(range(len(labels)), labels)
    plt.ylabel(ylab)
    plt.xticks(rotation=85)
    plt.gcf().subplots_adjust(bottom=0.30)
    fig.tight_layout()

    # Save the image so we can display it
    serverSave(fig, fname)

# GENERAL #
def serverSave(figObj, fname):
    path = 'static/' + fname
    figObj.savefig(path)
    Image.open(path).save(path, 'JPEG')

def getQueryFromFile(fname):
    with open('/home/jakeh/school/databases/CINS370Site/static/queries/' + fname, 'r') as f:
        return f.read()

def randFName():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
