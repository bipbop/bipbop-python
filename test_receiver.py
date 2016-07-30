import tornado.ioloop
import tornado.web

import xml.etree.ElementTree as ET

import bipbop

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        self.receiver = bipbop.client.Receiver(self.request.headers)
        xml = self.receiver.document(self.request.body)

        print ET.tostring(xml.getroot())

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()