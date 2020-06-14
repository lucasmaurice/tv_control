from http.server import BaseHTTPRequestHandler
from tv_serial import TvSerial

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
    
    def do_POST(self):
        return
    
    def do_GET(self):
        if self.path == "/on":
            print("Will Turn On!")
            out = TvSerial.writeCommandAsync("POWR0001")
            self.wfile.write(self.handle_http(200, "text/html", out))
        elif self.path == "/off":
            print("Will Turn Off!")
            out = TvSerial.writeCommandAsync("POWR0000")
            self.wfile.write(self.handle_http(200, "text/html", out))
        elif self.path == "/mute":
            print("Will Turn Off Audio!")
            out = TvSerial.writeCommandAsync("MUTE0001")
            self.wfile.write(self.handle_http(200, "text/html", out))
        elif self.path == "/unmute":
            print("Will Turn On Audio!")
            out = TvSerial.writeCommandAsync("MUTE0000")
            self.wfile.write(self.handle_http(200, "text/html", out))
        elif self.path == "/status":
            print("Will get status!")
            out = TvSerial.writeCommand("POWR   ?")
            self.wfile.write(self.handle_http(200, "text/html", out))
        else:
            print(self.path)
            self.wfile.write(self.handle_http(400, "text/html", "BAD REQUEST!"))
    
    def handle_http(self, status, content_type, text):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()
        return bytes(text, "UTF-8")
