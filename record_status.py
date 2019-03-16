#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/16
@Author  : wangjh
@desc    : PyCharm
"""
from base.handle_redis import HandleRedis

hr = HandleRedis(5)
def data_to_redis(task_id, status_code):
    table = task_id
    status = {
        'task_id': task_id,
        'status_code': status_code
    }
    hr.cache_str_redis(table, status)

if __name__ == '__main__':
    pass