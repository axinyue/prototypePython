import tornado.ioloop
import tornado.web
import tornado.options
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from multiprocessing import Process
from setting import REDIS_CONFIG,SVRVER_PORT
from url.url import urls
from uuid import uuid4
import os
import sys
current_path = os.path.dirname(__file__)

class Application(tornado.web.Application):             # 配置
    def __init__(self):

        setting = {
            "handlers":urls,
            "redis":REDIS_CONFIG,
            "cookie_secret":str(12345566666),
            "static_path":os.path.join(current_path, "static"),
            "template_path":os.path.join(current_path, "static"),
            }
        super(Application,self).__init__(**setting)


class RunServer():
    def  __init__(self,port):
        self.port = port
        app = self._make_app()
        self.server = HTTPServer(app)
        self.server.bind(self.port)

    def _make_app(self):
        return Application()

    def start(self): # TODO 增加端口号配置
        # tornado.options.parse_command_line()
        self.server.start(0)
        IOLoop.current().start()

class RunServer2():
    def  __init__(self,port):
        self.port = port
        app = self._make_app()
        app.listen(port)


    def _make_app(self):
        return Application()

    def start(self): # TODO 增加端口号配置
        # tornado.options.parse_command_line()
        IOLoop.current().start()

if __name__ == "__main__":
    try:

        cmd = sys.argv[1]
        if cmd=="-h":
            print("命令:\n -t 测试服务器\n -a 多线程服务器")
        elif cmd=="-t":
            RunServer2(SVRVER_PORT).start()
        elif cmd=="-a":
            RunServer(SVRVER_PORT).start()
        else:
            print("命令:\n -t 测试服务器\n -a 多线程服务器")

    except:
        print("Use default Server")
        RunServer2(SVRVER_PORT).start()
