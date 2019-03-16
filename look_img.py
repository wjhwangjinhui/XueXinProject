#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/16
@Author  : wangjh
@desc    : PyCharm
"""
import base64


def strToImage(str, filename):
    image_str = str.encode('ascii')
    image_byte = base64.b64decode(image_str)
    image_json = open(filename, 'wb')
    image_json.write(image_byte)
    image_json.close()


file_address = 'a.png'
strToImage(b, file_address)
