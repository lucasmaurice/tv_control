from http.server import BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    power_status = None
    mute_status = None
    req_power_status = None
    req_mute_status = None

    def do_HEAD(self):
        return
    
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        body = self.rfile.read(content_len)
        print(body)
        if body == b'1':
            Server.req_power_status = True
            self.wfile.write(self.handle_http(200, "text/html", "GG"))
        elif body == b'0':
            Server.req_power_status = False
            self.wfile.write(self.handle_http(200, "text/html", "GG"))
        else:
            self.wfile.write(self.handle_http(400, "text/html", "BAD REQUEST!"))

    def do_GET(self):
        if self.path == "/on":
            Server.req_power_status = True
            self.wfile.write(self.handle_http(200, "text/html", "GG"))
        elif self.path == "/off":
            Server.req_power_status = False
            self.wfile.write(self.handle_http(200, "text/html", "GG"))
        elif self.path == "/mute":
            Server.req_mute_status = True
            self.wfile.write(self.handle_http(200, "text/html", "GG"))
        elif self.path == "/unmute":
            Server.req_mute_status = False
            self.wfile.write(self.handle_http(200, "text/html", "GG"))
        elif self.path == "/status" or self.path == "/api":
            self.wfile.write(self.handle_http(200, "text/html", '1' if Server.power_status else '0'))
        else:
            print(self.path)
            self.wfile.write(self.handle_http(400, "text/html", "BAD REQUEST!"))
    
    def handle_http(self, status, content_type, text):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(text, "UTF-8")
