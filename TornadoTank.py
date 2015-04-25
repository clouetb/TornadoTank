import tornado.ioloop
import tornado.web
import tornado.websocket
import tornado.tcpserver
import tornado.tcpclient
import tornado.httpclient
import tornado.iostream
import tornado.gen
import uuid
import json
import logging
import urlparse
from tornado.options import define, options, parse_command_line


define("port", default=8888, help="run on the given port", type=int)
log = logging.getLogger("tornado.application")
log.setLevel(logging.DEBUG)

clients = dict()


class ForwardingRequestHandler(tornado.web.RequestHandler):
    def initialize(self, **dict):
        log.debug("Init data: %s", dict)
        split_url = urlparse.urlsplit(dict["url"])
        self.host = split_url.hostname
        self.port = split_url.port
        self.uri = split_url.path

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        log.debug("Browser sent: %s", self.request)
        host = "lwsnb160-cam.cs.purdue.edu"
        uri = "/axis-cgi/mjpg/video.cgi"
        client = tornado.tcpclient.TCPClient()
        stream = yield client.connect(self.host, self.port or 80)
        stream.write("GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" % (self.uri, self.host))
        headers = yield stream.read_until(b"\r\n\r\n")
        self.clear_header("Content-Type")
        for line in headers.split(b"\r\n"):
            parts = line.split(b":")
            if len(parts) == 2:
                self.add_header(parts[0].strip(), parts[1].strip())
        while True:
            chunk = yield stream.read_bytes(1500)
            self.write(chunk)
            self.flush()


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        uid = uuid.uuid1()
        url = "http://%s" % self.request.host
        log.debug("Serving index.html to %s", uid)
        self.render("templates/index.html", guid=uid, current_url=url)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    def ping(self, value):
        log.debug("Received a ping from %s responding to this client", value)
        self.write_message("Ping to " + value)

    def set_direction(self, value):
        log.debug("Changed direction to %s", value)
        self.write_message("Setting direction to '%s'" % value)

    def set_speed(self, value):
        log.debug("Changed speed to %s", value)
        self.write_message("Setting speed to %d" % value)

    message_types = {
        "ping": ping,
        "direction": set_direction,
        "speed": set_speed
    }

    def open(self, *args):
        self.id = self.get_argument("id")
        self.stream.set_nodelay(True)
        clients[self.id] = {"id": self.id, "object": self}
        log.debug("Connection from %s", self.id)
        self.write_message("Connection from " + self.id)

    def on_message(self, message):
        log.debug("Client %s received a message : %s", self.id, message)
        actions = json.loads(message)
        for k in actions.keys():
            self.message_types[k](self, actions[k])

    def on_close(self):
        if self.id in clients:
            del clients[self.id]

target_url = "http://lwsnb160-cam.cs.purdue.edu/axis-cgi/mjpg/video.cgi"

app = tornado.web.Application([
    (r'/', IndexHandler),
    (r'/socket', WebSocketHandler),
    (r'/video_stream', ForwardingRequestHandler, dict(url=target_url))
], debug=True)

if __name__ == '__main__':
    parse_command_line()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()