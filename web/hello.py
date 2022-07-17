def app(env, start_response):
    params = '\n'.join(env['QUERY_STRING'].split('&'))
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return bytes(params)
