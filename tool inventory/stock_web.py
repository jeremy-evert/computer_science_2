from http.server import HTTPServer, BaseHTTPRequestHandler
from stock import wrenches

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(
            f"<h1> Pipe Wrench stock = {wrenches}</h1>".encode()
        )

server = HTTPServer(("127.0.0.1", 8000), MyHandler)

print("Server running at http://127.0.0.1:8000")

try:
    server.serve_forever()
except KeyboardInterrupt:
    print("Stopping server...")
    server.server_close()
    