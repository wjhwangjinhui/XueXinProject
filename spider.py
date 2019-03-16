#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/16
@Author  : wangjh
@desc    : PyCharm
"""
from get_data import login, save_xj, save_xl
from parse_data import last_data
from record_status import data_to_redis
from mylog import log


def start_spider(username, password, task_id):
    s = login(username, password)
    data_to_redis(task_id, 2000)
    try:
        save_xj(s, username)
    except Exception as e:
        data_to_redis(task_id, 3002)
        log.crawler.error('xj:{}'.format(e))
    try:
        save_xl(s, username)
    except Exception as e:
        data_to_redis(task_id, 3002)
        log.crawler.error('xl:{}'.format(e))
    data = last_data(username)
    data_to_redis(task_id, 3001)
    return data


if __name__ == '__main__':
    pass
