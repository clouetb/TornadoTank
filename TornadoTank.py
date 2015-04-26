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
import sys
import urlparse
from tornado.options import define, options, parse_command_line

import PruioTank
import mjpg_streamer_wrapper

define("port", default=8888, help="run on the given port", type=int)
log = logging.getLogger("tornado.application")
log.setLevel(logging.DEBUG)

clients = dict()

m1_left_motor_direction = "P8_14"
m1_left_motor_pwm = "P8_13"
m2_right_motor_direction = "P9_13"
m2_right_motor_pwm = "P9_14"
tank = PruioTank.Tank(m1_left_motor_direction, m1_left_motor_pwm, m2_right_motor_direction, m2_right_motor_pwm)

class ForwardingRequestHandler(tornado.web.RequestHandler):
    def initialize(self, **dict):
        log.debug("Init data: %s", dict)
        split_url = urlparse.urlsplit(dict["url"])
        self.host = split_url.hostname
        self.port = split_url.port or 80
        self.uri = split_url.path
        self.query = split_url.query
        log.debug("Parameters: %s , %s , %s , %s", self.host, self.port, self.uri, self.query)

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        log.debug("Browser sent: %s", self.request)
        client = tornado.tcpclient.TCPClient()
        stream = yield client.connect(self.host, self.port)
        stream.write("GET %s?%s HTTP/1.1\r\nHost: %s\r\n\r\n" % (self.uri, self.query, self.host))
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
        host_port = self.request.host
        log.debug("Serving index.html to %s", uid)
        self.render("templates/index.html", guid=uid, host_port=host_port)


class WebSocketHandler(tornado.websocket.WebSocketHandler):
    global tank

    def ping(self, value):
        log.debug("Received a ping from %s responding to this client", value)
        self.write_message("Ping to " + value)

    def set_direction(self, value):
        log.debug("Changing direction to %s for %s", value, tank)
        tank.set_direction(value)
        self.write_message("Setting direction to '%s'" % value)

    def set_speed(self, value):
        log.debug("Changing speed to %s for %s", value, tank)
        speed = int(value) / float(100) or float(0)
        tank.set_speed(speed)
        self.write_message("Setting speed to %f" % speed)

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

#target_url = "http://lwsnb160-cam.cs.purdue.edu/axis-cgi/mjpg/video.cgi"
target_url = "http://localhost:8090/?action=stream"
app = tornado.web.Application([
        (r'/socket', WebSocketHandler),
        (r'/video_stream', ForwardingRequestHandler, dict(url=target_url)),
        (r'/', IndexHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": "templates"})
    ], debug=True)

if __name__ == '__main__':
    try:
        log.info("Starting application")
        log.debug("Starting streaming server")
        mjpg_streamer_wrapper.start_streamer()
        parse_command_line()
        app.listen(options.port)
        log.debug("Starting Tornado server")
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        log.info("Shutting down application")
        log.debug("Stopping Tornado server")
        tornado.ioloop.IOLoop.instance().stop()
        log.debug("Stopping streaming server")
        mjpg_streamer_wrapper.stop_streamer()
        log.info("Shutting down, deleting tank %s instance", tank)
        del tank
        log.info("Application stopped")
        sys.exit(0)