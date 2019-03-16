#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/16
@Author  : wangjh
@desc    : PyCharm
"""
import os
import sys

cur_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(cur_dir))
from flask import Flask, request, jsonify
from spider import start_spider
from record_status import data_to_redis
from base.handle_mongo import save_data_in_mongo

app = Flask(__name__)


@app.route('/xuexin', methods=['POST'])
def index():
    username = request.form.get('username')
    password = request.form.get('password')
    task_id = request.form.get('task_id')
    data_to_redis(task_id, 1)
    data = start_spider(username, password, task_id)
    d = {
        'taskid': task_id,
        'result': data
    }
    save_data_in_mongo(d, "xuexin")
    return jsonify(data)


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8889)
