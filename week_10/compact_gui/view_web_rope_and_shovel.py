"""The WEB view for two items. Same model, same idea as view_rope_and_shovel.py.

Run:  python3 view_web_rope_and_shovel.py     (Windows: py -3 ...)
Then open  http://localhost:8000   Python standard library only; no installs.

SAME IDEA, DIFFERENT SYNTAX (Tkinter  ->  web):
    tk.Tk() window ................ the browser tab + HTTPServer
    tk.Label + StringVar .......... HTML text, rebuilt from the model on every request
    tk.Button(command=handler) .... <form action="/restock/rope"> + a route to a handler
    on_restock_rope() ............. on_restock_rope()          (same function, same job!)
    refresh() ..................... render_page()              (ask the MODEL, build the view)
    root.mainloop() ............... server.serve_forever()     (wait for events forever)
    EVENT = a mouse click ......... EVENT = an HTTP request arriving
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from inventory_rope_and_shovel import Inventory   # the SAME model file, untouched

# ---- OBJECT: one model holds both counts (same as the Tkinter view) ----
model = Inventory()


# ---- VIEW: Tkinter used Labels; here the "labels" are HTML, rebuilt every time ----
def render_page():
    """Ask the MODEL for every number, then build the page. No rules here."""
    return f"""<!doctype html><title>Inventory</title>
<p>Rope: {model.count('rope')}</p>
<p>Shovel: {model.count('shovel')}</p>
<p>Total: {model.total()}</p>
<form method="post" action="/restock/rope"><button>Restock Rope</button></form>
<form method="post" action="/restock/shovel"><button>Restock Shovel</button></form>"""


# ---- HANDLERS: identical to the Tkinter version. Only the refresh step differs. ----
def on_restock_rope():
    model.restock("rope")            # 1. ROUTE the event to the model


def on_restock_shovel():
    model.restock("shovel")          # same pattern, different item


# ---- THE PAIRINGS: Tkinter wrote command=on_restock_rope on a button.
#      The web has no button-to-function wire, so we keep a table: URL path -> handler. ----
ROUTES = {
    "/restock/rope": on_restock_rope,       # PAIR 1
    "/restock/shovel": on_restock_shovel,   # PAIR 2
}


class Handler(BaseHTTPRequestHandler):
    """The event source. Each request that arrives is one event."""

    def do_GET(self):                # the browser asking to SEE the page
        self._send_page()

    def do_POST(self):               # the browser reporting a click on a form button
        handler = ROUTES.get(self.path)
        if handler is None:
            self.send_error(404)
            return
        handler()                    # call the SAME kind of handler as in Tkinter
        self.send_response(303)      # 2. REFRESH: tell the browser to reload the page
        self.send_header("Location", "/")
        self.end_headers()

    def _send_page(self):
        body = render_page().encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = HTTPServer(("127.0.0.1", 8000), Handler)   # 127.0.0.1 = this computer only
    server.serve_forever()           # wait for events forever; each request is one event
