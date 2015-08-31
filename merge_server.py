import http.server
import argparse
from hooks_handler import GitHubHooksHandler

parser = argparse.ArgumentParser()
parser.add_argument('host', nargs='?', default='127.0.0.1', help='The ip address to host the merge_server at.')
parser.add_argument('port', nargs='?', type=int, default=8080, help='The port to host the merge_server at.')
args = parser.parse_args()

handler = GitHubHooksHandler
PORT = args.port
host = args.host

server = http.server.HTTPServer((host, PORT), handler)
try:
    print('Start')
    server.serve_forever()
except KeyboardInterrupt:
    pass

print('Done')

