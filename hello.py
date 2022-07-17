def app(env, start_response):
    params = [bytes(i + '\n', 'ascii') for i in env['QUERY_STRING'].split('&')]
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return params
