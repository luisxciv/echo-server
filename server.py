from bottle import Bottle, request, response, run
from json import dumps
import json

app = Bottle()

@app.hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@app.route('/data', method=['OPTIONS', 'GET', 'POST', 'DELETE', 'PATCH', 'PUT'])
def data():
    """
    """
    response.content_type = 'application/json'
    if request.method == 'GET' or 'DELETE':
            data = request.body.read()
            try:
                rv = {"method": request.method, "data": json.loads(data.decode('utf-8'))}
            except:
                raise ValueError('Data formatted incorrectly')
            return dumps(rv)
    else:
        return dumps({"method": request.method, "data": request.json})


if __name__ == '__main__':
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("--host", dest="host", default="localhost",
                      help="hostname or ip address", metavar="host")
    parser.add_option("--port", dest="port", default=8080,
                      help="port number", metavar="port")
    (options, args) = parser.parse_args()
    run(app, host=options.host, port=int(options.port))