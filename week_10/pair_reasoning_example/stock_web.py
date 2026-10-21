from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser

from stock import toilet_paper

URL = "http://127.0.0.1:8000"


class StockPage(BaseHTTPRequestHandler):
    def do_GET(self):
        # Keep the response as one simple page for this small example.
        page = f"<!doctype html><html><body><h1>toilet paper stock = {toilet_paper}</h1></body></html>"
        body = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


server = HTTPServer(("127.0.0.1", 8000), StockPage)
print(f"Serving stock at {URL} (press Ctrl+C to stop)")
webbrowser.open(URL)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
finally:
    server.server_close()
