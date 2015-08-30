import http.server
from hooks_handler import GitHubHooksHandler


handler = GitHubHooksHandler
PORT = 8080
host = '127.0.0.1'

server = http.server.HTTPServer((host, PORT), handler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    pass

print('Done')

