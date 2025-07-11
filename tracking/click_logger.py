from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class ClickHandler(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        self.send_response(200)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        click = json.loads(data.decode('utf-8'))

        with open("click_logs.json", "a") as f:
            f.write(json.dumps(click) + "\n")

server = HTTPServer(('localhost', 3000), ClickHandler)
print("✅ Listening on port 3000...")
server.serve_forever()
