from http.server import BaseHTTPRequestHandler, HTTPServer

def add_numbers(a, b):
    return a + b

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        result = add_numbers(2, 3)
        self.wfile.write(f"Hello CI/CD! 2 + 3 = {result}".encode("utf-8"))

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 3010), MyHandler)
    print("Server started on port 3010...")
    server.serve_forever()
