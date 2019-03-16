#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/16
@Author  : wangjh
@desc    : PyCharm
"""
import os
import requests
from lxml import etree
from parse_img import ocr_img


def img(s, url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'
    }
    res = s.get(url=url, headers=headers)
    with open(filename, 'wb') as file:
        file.write(res.content)


def login(username, password):
    s = requests.session()
    url = 'https://account.chsi.com.cn/passport/login?service=https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Fj_spring_cas_security_check'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'
    }
    res1 = s.get(url=url, headers=headers)
    content = res1.text
    tree = etree.HTML(content)
    lt = tree.xpath('//*[@id="fm1"]/input[1]/@value')[0]
    execution = tree.xpath('//*[@id="fm1"]/input[2]/@value')[0]
    data = {
        'username': username,
        'password': password,
        'submit': '登  录',
        'lt': lt,
        'execution': execution,
        '_eventId': 'submit'
    }
    s.post(url=url, data=data, headers=headers)
    f = os.getcwd()
    f1 = os.path.join(f, 'img')
    f2 = os.path.join(f1, str(username))
    os.mkdir(f2)
    return s


def save_xj(s, username):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'
    }
    r = s.get(url='https://my.chsi.com.cn/archive/gdjy/xj/show.action', headers=headers)
    con = r.text
    tree = etree.HTML(con)
    xjs = tree.xpath("//div[@class='main']/div[contains(@class,'clearfix')]")
    f = os.getcwd()
    file1 = os.path.join(f, 'img')
    file2 = os.path.join(file1, str(username))
    for clf in xjs:
        filename = os.path.join(file2, 'title.png')
        mb_title = clf.xpath('./div/div/img/@src')[0]
        img(s, mb_title, filename)
        titles = ocr_img(filename)
        title = titles[0]
        xjxx_img = clf.xpath('./div/div/div/img[2]/@src')[0]
        filename1 = os.path.join(file2, title + '_xj.png')
        img(s, xjxx_img, filename1)

        lq_img_n = clf.xpath('./div/div/div/div[1]/img/@src')[0]
        if lq_img_n[0:4] == 'http':
            filename2 = os.path.join(file2, title + '_xjlq.png')
            img(s, lq_img_n, filename2)
        else:
            lq_img_n = 'https://my.chsi.com.cn' + lq_img_n
            filename2 = os.path.join(file2, title + '_xjlq.png')
            img(s, lq_img_n, filename2)

        by_img_n = clf.xpath('./div/div/div/div[2]/img/@src')[0]
        if by_img_n[0:4] == 'http':
            filename3 = os.path.join(file2, title + '_xjby.png')
            img(s, by_img_n, filename3)
        else:
            by_img_n = 'https://my.chsi.com.cn' + by_img_n
            filename3 = os.path.join(file2, title + '_xjby.png')
            img(s, by_img_n, filename3)


def save_xl(s, username):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.64 Safari/537.36'
    }
    r = s.get(url='https://my.chsi.com.cn/archive/gdjy/xl/show.action', headers=headers)
    con = r.text
    tree = etree.HTML(con)
    xls = tree.xpath("//div[@class='main']/div[contains(@class,'clearfix')]")
    f = os.getcwd()
    file1 = os.path.join(f, 'img')
    file2 = os.path.join(file1, str(username))
    for clf in xls:
        filename = os.path.join(file2, 'title.png')
        mb_title = clf.xpath('./div/div/img/@src')[0]
        img(s, mb_title, filename)
        titles = ocr_img(filename)
        title = titles[0]
        xjxx_img = clf.xpath('./div/div/div[2]/img[2]/@src')[0]
        filename1 = os.path.join(file2, title + '_xl.png')
        img(s, xjxx_img, filename1)

        zs_img_n = clf.xpath('./div/div/div[1]/div/img/@src')[0]
        if zs_img_n[0:4] == 'http':
            filename2 = os.path.join(file2, title + '_xlzs.png')
            img(s, zs_img_n, filename2)
        else:
            zs_img_n = 'https://my.chsi.com.cn' + zs_img_n
            filename2 = os.path.join(file2, title + '_xlzs.png')
            img(s, zs_img_n, filename2)


if __name__ == '__main__':
    username = '账号'
    password = '密码'
    s = login(username, password)
    save_xj(s, username)
    save_xl(s, username)
