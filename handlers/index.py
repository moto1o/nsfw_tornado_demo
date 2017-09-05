#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import copy

from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine
from open_nsfw import classify_nsfw


class IndexHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
        self.settings['total'] = self.settings['total'] + 1
        url = self.get_argument("url", None)
        image_data = None

        if url is not None:
            http_client = AsyncHTTPClient()
            response = yield http_client.fetch(url)

            print "response.code", response.code
            if response.code == 200:
                image_data = response.buffer.read()
                caffe_transformer = copy.deepcopy(
                    self.settings['caffe_transformer'])
                caffe_net = self.settings['caffe_net']

                scores = classify_nsfw.caffe_preprocess_and_compute(
                    image_data, caffe_transformer=caffe_transformer,
                    caffe_net=caffe_net, output_layers=['prob'])

                # Scores is the array containing SFW / NSFW image probabilities
                # scores[1] indicates the NSFW probability
                print "NSFW score:  ", scores[1]
                self.write("NSFW score:  " + str(scores[1]))

                print "total", self.settings['total']
            # else:
            #    print "response.code", response.code
        else:
            print "NSFW score:  ", None
            # self.write("NSFW score:  ")

        self.write("ok ==> responses end")
        self.finish()

    def post(self):
        self.write("Hello, world")
        self.finish()
