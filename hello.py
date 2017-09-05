#!/usr/bin/env Python
# coding:utf-8

# tornado.httpserver：这个模块就是用来解决 web 服务器的 http 协议问题，它提供了不少属性方法，实现客户端和服务器端的互通。
# Tornado 的非阻塞、单线程的特点在这个模块中体现。
# tornado.ioloop：这个也非常重要，能够实现非阻塞 socket 循环，不能互通一次就结束呀。
# tornado.options：这是命令行解析模块，也常用到。
# tornado.web：这是必不可少的模块，它提供了一个简单的 Web 框架与异步功能，从而使其扩展到大量打开的连接，使其成为理想的长轮询。
# import tornado.httpserver
# import tornado.ioloop
# import tornado.options
# import tornado.web

import time
while True:
    print("sleep 1000")
    time.sleep(1000)
