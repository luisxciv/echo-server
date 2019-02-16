from bottle import Bottle, request, response, run

app = Bottle()


@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, PATCH, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'


@app.route('/data', method=['OPTIONS', 'GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def data():
    if request.method == 'OPTIONS':
        response.status = 200
        return {''}
    elif request.method == 'GET':
        return {'method': request.method, 'data': 'GET data'}
    elif request.method == 'POST':
        data = request.json.get('data')
        return {'method': request.method, 'data': data}
    elif request.method == 'DELETE':
        return {'method': request.method, 'data': 'DELETE data'}
    elif request.method == 'PUT':
        data = request.json.get('data')
        return {'method': request.method, 'data': data}
    elif request.method == 'PATCH':
        data = request.json.get('data')
        return {'method': request.method, 'data': data}


@app.route('/data/<data>', method=['OPTIONS', 'GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def data(data):
    if request.method == 'OPTIONS':
        response.status = 200
        return {'test'}
    elif request.method == 'DELETE':
        return {'method': request.method, 'data': data}
    elif request.method == 'GET':
        return {'method': request.method, 'data': data}


if __name__ == '__main__':
    from optparse import OptionParser

    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost",
                      help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=8080,
                      help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port))
