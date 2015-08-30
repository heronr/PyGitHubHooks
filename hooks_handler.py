import http.server
import http.client
import json
from git_hub_events import *

class GitHubHooksHandler(http.server.BaseHTTPRequestHandler):

    def finish_response(response_code):
        self.send_response(response_code)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()

    #
    # Handler for the get request
    #
    def do_GET(self):
        self.finish_response(http.client.OK)
        return None
    #
    # Handler for the post request
    #     
    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        event_type = self.headers.get('X-Github-Event', '')
        if len(event_type) == 0:
            self.finish_response(http.client.BAD_REQUEST)
            return

        real_type = GetEventType(event_type)
        if real_type == None:
            self.finish_response(http.client.BAD_REQUEST)
            return

        if content_length <= 0:
            self.finish_response(http.client.NO_CONTENT)
            return

        content = self.rfile.read(content_length)
        content_str = content.decode('utf8')
        json_object = json.loads(content_str)
        print(json_object)
        switcher = {
            'push' : HandlePushEvent,
            'ping' : HandlePingEvent,
        }
        method = switcher.get(real_type.name, lambda: False)
        method_result = method()
        if method_result:
            self.finish_response(http.client.OK)
        else:
            self.finish_response(http.client.BAD_REQUEST)