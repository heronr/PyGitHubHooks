import http.server
import json

class GitHubHooksHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        print('Got GET!')
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        return None
        
    def do_POST(self):
        print('Got POST!')
        #print(self.headers)
        content_length = int(self.headers.get('content-length', 0))
        if content_length > 0:
            content = self.rfile.read(content_length)
            print(content)
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
