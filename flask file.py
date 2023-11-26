import urllib
import json
import os
from flask import Flask , request , make_response , jsonify
from prediction import prediction
app = Flask(__name__)

@app.route('/webhook', methods = ['POST', 'GET'])
def webhook():
    if request.method == "POST":
        req = request.get_json(silent = True , force = True)
        res = req['queryResult']['parameters']
        res = processRequest(req)
        res = json.dumps(res , indent=4)
        r = make_response(res)
        r.headers['Content-Type'] = 'application/json'
        return r

def processRequest(req):
    query_response = req['queryResult']
    action_name = query_response.get('action')
    print(query_response)
    text = query_response.get('queryText', None)

    parameters = query_response.get('parameters', None)
    nada=prediction(text)
    return {"fulfillmentText":nada}

    
if __name__ == '__main__':
    app.run(debug=True)
