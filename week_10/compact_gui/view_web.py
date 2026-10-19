"""Pass 2: the same Inventory model behind a web page. Python standard library only.

Run:  python3 view_web.py     then open  http://localhost:8000
Event: browser POSTs /restock -> handler -> model.restock -> page shows the new count.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from inventory import Inventory

model = Inventory()

PAGE = """<!doctype html><title>Inventory</title>
<p>Items: {n}</p>
<form method="post" action="/restock"><button>Restock</button></form>"""


class Handler(BaseHTTPRequestHandler):
    def _show(self):
        body = PAGE.format(n=model.count()).encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        self._show()

    def do_POST(self):
        if self.path == "/restock":
            n = model.restock("rope")                       # route to the model
            print(f"request -> handler -> model.restock -> {n} items")
            self.send_response(303)                         # then refresh the view
            self.send_header("Location", "/")
            self.end_headers()
        else:
            self.send_error(404)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8000), Handler).serve_forever()
