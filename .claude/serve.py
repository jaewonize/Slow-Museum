import functools
import http.server
import socketserver

DIRECTORY = "/Users/ttt/Desktop/Slow Museum"
PORT = 8766

Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIRECTORY)


class Server(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True


with Server(("127.0.0.1", PORT), Handler) as httpd:
    httpd.serve_forever()
