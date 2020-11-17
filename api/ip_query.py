from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = str(self.path)
    try:
        domain = path[path.rindex("/")+1:]
        print(domain)
        ip = socket.gethostbyname(domain)   
    except:
        text = 'path is: %s, \n Error happens\n'%(path)
    else:
        text = 'domain is: %s \n ip is: %s\n'%(domain, ip)
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    self.wfile.write(text.encode())
    return

if __name__ == "__main__":
    http_server = HTTPServer(('', int(8888)), handler)
    http_server.serve_forever() 