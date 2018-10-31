import re, werkzeug.datastructures
from flask import Flask, request, json
import logging

app = Flask(__name__)

def decodeForJSON(valor):
    if isinstance(valor, list):
        if len(valor) > 1:
            valor = [decodeForJSON(i) for i in valor]
        else:
            valor = decodeForJSON(valor[0])
    else:    
        if valor == '':
            valor = None
        elif ([valor.upper()] == ['TRUE']):
            valor = True
        elif ([valor.upper()] == ['FALSE']):
            valor = False
        elif re.match(r'^[-+]?[0-9]+$', str.strip(valor)):
            valor = int(valor)
        elif re.match(r'^[-+]?([0-9]+|[0-9]+\.[0-9]*|[0-9]*\.[0-9]+)$', str.strip(valor)):
            valor = float(str.strip(valor))
    return valor  

def ArgsToJSon(argsGET):
    DiccionarioArgs = dict([(K, decodeForJSON(V)) for (K,V) in argsGET.lists()])
    return json.dumps(DiccionarioArgs)

@app.route("/")
def home():
    logging.basicConfig(filename='app.log', level=logging.INFO)
    logging.info('Started ' + str(request.full_path))# .args.to_dict(flat=False)))
    #request.parameter_storage_class = werkzeug.datastructures.ImmutableMultiDict
    MiJSon = ArgsToJSon(request.args)
    #print(MiJSon)
    response = app.response_class(
        response= MiJSon,
        status=200,
        mimetype='application/json',
        content_type='application/json'
        )
    return response 