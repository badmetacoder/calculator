import tornado.ioloop
import tornado.web
import calculator

class CalculateHandler(tornado.web.RequestHandler):
    def post(self):
        c = calculator.simple.SimpleCalculator()

        try:
            c.run(self.request.body)
            for i in c.log:
                self.write("%s\n" % str(i).encode('utf-8'))

        except Exception as e:
            self.send_error()

application = tornado.web.Application([
    (r"/v1/calculate", CalculateHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
