#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/16
@Author  : wangjh
@desc    : PyCharm
"""
from aip import AipOcr

APP_ID = 'xxx'
API_KEY = 'xxx'
SECRET_KEY = 'xxx'


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


def ocr_img(img_file):
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    image = get_file_content(img_file)
    ocr_data = client.basicAccurate(image)
    words_result = ocr_data['words_result']
    data = []
    for words in words_result:
        a = words['words']
        data.append(a)
    return data


if __name__ == '__main__':
    img_file = 'index4.png'
    data = ocr_img(img_file)
    print(data)
