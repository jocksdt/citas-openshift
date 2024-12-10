import flask
from flask import jsonify, make_response
import random
import os
import socket
import json
import sys
import MySQLdb

quotes = []
quoteCount = 0

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return prepareResponse(jsonify("qotd"))

@app.route('/version', methods=['GET'])
def version():
    response = make_response("v2")
    response.mimetype = "text/plain"
    return prepareResponse(response)
@app.route('/writtenin', methods=['GET'])
def writtenin():
    response = make_response("Python 3.9")
    response.mimetype = "text/plain"
    return prepareResponse(response)

@app.route('/health', methods=['GET'])
def health():
    return 'foo'

@app.route('/quotes', methods=['GET'])
def getQuotes():
    quotes = getQuotes()
    return prepareResponse(jsonify(quotes))
  
@app.route('/quotes/<int:id>', methods=['GET'])
def getQuoteById(id):
    return prepareResponse(jsonify(replaceHostname(getQuotes()[id])))

@app.route('/quotes/random', methods=['GET'])
def getRandom():
    quotes = getQuotes()
    n = random.randint(0,len(quotes)-1)
    return prepareResponse(jsonify(replaceHostname(quotes[n])))
    
def prepareResponse(response):
    # Enable Access-Control-Allow-Origin
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

def replaceHostname(jsondoc):
    q = json.dumps(jsondoc)
    q = q.replace('-hostname-', socket.gethostname())
    return json.loads(q)

def getQuotes():
    quotes=[]
    try:
        conn = MySQLdb.connect(
            user=os.environ['USER_DB'],
            password=os.environ['PASSWORD_DB'],
            host=os.environ['HOST_DB'],
            database="citas",
            port=3306)
        mycursor = conn.cursor()
        mycursor.execute("SELECT '-hostname-' as hostname, id, quotation, author FROM quotes ORDER BY author, id")
        quotes = mycursor.fetchall()
        result_dict = {}
        for i, row in enumerate(quotes):
            row_dict = {}
            for j, col in enumerate(mycursor.description):
                row_dict[col[0]] = row[j]
            result_dict[i] = row_dict
        quotes=result_dict
        conn.close()
    except:
        sys.exit(1)
    return quotes

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
