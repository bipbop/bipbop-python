import tornado.ioloop
import tornado.web

import bipbop

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.receiver = bipbop.client.Receiver(self.request.headers)
        self.receiver.document()
        # print repr(self.request)

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()