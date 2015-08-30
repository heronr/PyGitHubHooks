import http.server
import http.client
import json
from git_hub_events import *

class GitHubHooksHandler(http.server.BaseHTTPRequestHandler):

    def finish_response(self, response_code, error_msg=''):
        self.send_response(response_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
        if len(error_msg):
            print(error_msg)
            self.wfile.write("<html><body><p>{}</p></body></html>".format(error_msg).encode('utf8'))

    #
    # Handler for the post request
    #     
    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        event_str = self.headers.get('X-Github-Event', '')
        if len(event_str) == 0:
            self.finish_response(http.client.BAD_REQUEST, 'Request has no Github event type')
            return

        event_type = GetEventType(event_str)
        if event_type == None:
            self.finish_response(http.client.BAD_REQUEST, 'Unable to handle {} event'.format(event_str))
            return

        if content_length <= 0:
            self.finish_response(http.client.NO_CONTENT, 'Event {} had no post data'.format(event_str))
            return

        content = self.rfile.read(content_length)
        content_str = content.decode('utf8')
        json_object = json.loads(content_str)
        switcher = {
            'push' : HandlePushEvent,
            'ping' : HandlePingEvent,
        }
        method = switcher.get(event_type.name, lambda x: False)
        method_result = method(json_object)
        if method_result:
            self.finish_response(http.client.OK)
        else:
            self.finish_response(http.client.BAD_REQUEST, 'Event {} failed'.format(event_str))