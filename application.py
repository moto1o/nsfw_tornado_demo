#!/usr/bin/env Python
# coding=utf-8

from url import url
from open_nsfw import classify_nsfw

import tornado.web
import os
import sys  # utf-8，兼容汉字
reload(sys)
sys.setdefaultencoding("utf-8")

settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "statics"),
    total=1,
)
caffe = classify_nsfw.caffe_transformer_net_instance()
settings.update(caffe)

application = tornado.web.Application(
    handlers=url,
    **settings
)
