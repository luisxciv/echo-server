from bottle import run, post, request, response, get, route, put, delete, hook
from json import dumps


@get('/data')
def data_get():
    response.content_type = "application/json"
    return dumps({"method": request.method, "data": request.json})

@post('/data')
def data_post():
    response.content_type = "application/json"
    return dumps({"method": request.method, "data": request.json})

@delete('/data')
def data_delete():
    response.content_type = "application/json"
    return dumps({"method": request.method, "data": request.json})

@put('/data')
def data_put():
    response.content_type = "application/json"
    return dumps({"method": request.method, "data": request.json})

@route('/data', method='PATCH')
def data_patch():
    response.content_type = "application/json"
    return dumps({"method": request.method, "data": request.json})



run(host='localhost', port=8080, debug=True)

if __name__ == "__main__":
    run()