#!/usr/bin/env Python
# coding:utf-8

# tornado.httpserver：这个模块就是用来解决 web 服务器的 http 协议问题，它提供了不少属性方法，实现客户端和服务器端的互通。
# Tornado 的非阻塞、单线程的特点在这个模块中体现。
# tornado.ioloop：这个也非常重要，能够实现非阻塞 socket 循环，不能互通一次就结束呀。
# tornado.options：这是命令行解析模块，也常用到。
# tornado.web：这是必不可少的模块，它提供了一个简单的 Web 框架与异步功能，从而使其扩展到大量打开的连接，使其成为理想的长轮询。
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', welcome you to read: www.itdiffer.com')

if __name__ == "__main__":
    # tornado.options.parse_command_line(),这是在执行 tornado 的解析命令行。
    # 在 tornado 的程序中，只要 import 模块之后，就会在运行的时候自动加载，不需要了解细节，
    # 但是，在 main（）方法中如果有命令行解析，必须要提前将模块引入。
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
