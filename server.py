#!/usr/bin/env python3
from http.server import BaseHTTPRequestHandler, HTTPServer
from time import sleep


class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Mock a blocking server call.
        sleep(10)
        self.send_response(200)


def main():
    server = HTTPServer(("localhost", 8080), GetHandler)
    print("Starting server localhost:8080")
    server.serve_forever()


if __name__ == "__main__":
    main()
