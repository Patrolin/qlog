from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from typing import cast
from common import *
from io import BufferedReader

# https://security.stackexchange.com/questions/226095/pythons-http-server-library-basic-security-checks
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in ["/", "/index.html"]:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open("index.html", "rb") as f:
                self.wfile.write(f.read())
        elif self.path == "/id":
            self.send_response(200)
            self.send_header("Content-type", "text/json")
            self.end_headers()
            self.wfile.write(str(getNextId()).encode())
        else:
            self.send_response(404)

    def do_POST(self):
        try:
            print(self.path)
            length = int(self.headers.get("content-length") or "0")
            rfile = cast(BufferedReader, self.rfile)
            read_bytes = rfile.read(length)
            read = read_bytes.decode("utf8")
            sessionId = int(self.path[1:])
            with open(f"log/{sessionId}", "a+") as f:
                f.write(read + "\n")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(read_bytes or b"")
        except:
            self.send_response(500)

PORT = 8080
if __name__ == "__main__":
    mkdir("log")
    with ThreadingHTTPServer(("", PORT), MyRequestHandler) as httpd:
        #httpd.socket = ssl.wrap_socket(httpd.socket, certfile='localhost.pem', server_side=True)
        httpd.serve_forever()
