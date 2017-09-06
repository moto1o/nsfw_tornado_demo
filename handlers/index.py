#!/usr/bin/env Python
# coding=utf-8

import tornado.web
import json

from tornado.httpclient import AsyncHTTPClient
from tornado.gen import coroutine
from open_nsfw import classify_nsfw


class IndexHandler(tornado.web.RequestHandler):

    @coroutine
    def get(self):
        urls = self.get_arguments("url")
        responses = []
        responseDict = {'code': 200, 'data': responses}
        if urls:
            if len(urls) <= 5:
                for x in xrange(0, len(urls)):
                    responses.append(None)
                    url = urls[x]
                    try:
                        if url:
                            responses[x] = yield AsyncHTTPClient().fetch(url)
                    except Exception as e:
                        print('Exception: %s ' % (e,))
                        responses[x] = None
                for x in xrange(0, len(responses)):
                    response = responses[x]
                    if response and response.code == 200:
                        image_data = response.buffer.read()
                        caffe_transformer = self.settings['caffe_transformer']
                        caffe_net = self.settings['caffe_net']

                        scores = classify_nsfw.caffe_preprocess_and_compute(
                            image_data, caffe_transformer=caffe_transformer,
                            caffe_net=caffe_net, output_layers=['prob'])

                        responses[x] = scores[1]
                    else:
                        responses[x] = None
            else:
                responseDict['code'] = 400
                responseDict['msg'] = '最多处理5张图片'
        else:
            responseDict['code'] = 400
            responseDict['msg'] = '最少处理1张图片'

        self.set_header('Content-Type', 'application/json')
        self.write(json.dumps(responseDict))
        self.finish()
