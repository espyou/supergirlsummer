import http.server, socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='/Users/michaelhamilton/Desktop/Claude Cowork', **kwargs)

with socketserver.TCPServer(("", 3000), Handler) as httpd:
    httpd.serve_forever()
