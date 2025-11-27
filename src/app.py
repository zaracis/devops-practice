from http.server import BaseHTTPRequestHandler, HTTPServer


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        html = """<h1>✅ CI/CD works!</h1>
<p>Deployed via GitHub Actions</p>
<p><code>git push</code> &rarr; auto-deploy</p>"""
        self.wfile.write(html.encode("utf-8"))


if __name__ == "__main__":
    HTTPServer(("", 8080), Handler).serve_forever()
