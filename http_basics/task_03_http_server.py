#!/usr/bin/python3
""" Simple HTTP server using http.server """
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

if __name__ == "__main__":
    server = HTTPServer(('0.0.0.0', 8000), SimpleHandler)
    server.serve_forever()
