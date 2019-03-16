#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2019/3/16
@Author  : wangjh
@desc    : PyCharm
"""
import base64
import os
from parse_img import ocr_img

syllable = {
    '姓名': 'name',
    '性别': 'sex',
    '出生日期': 'birth_data',
    '民族': 'nation',
    '证件号码': 'cert',
    '学校名称': 'university',
    '层次': 'arrangement',
    '专业': 'major',
    '学制': 'schooling_length',
    '学历类别': 'education',
    '学习形式': 'learning_form',
    '分院': 'institute',
    '系(所、函授站)': 'faction',
    '班级': 'clazz',
    '学号': 'school_num',
    '入学日期': 'entrance_date',
    '离校日期': 'leave_date',
    '学籍状态': 'status',
    '毕(结)业日期': 'graduation_date',
    '毕(结)业': 'graduation',
    '校(院)长姓名': 'principal_name',
    '证书编号': 'certificate_num',
    '预计毕业日期': 'yjbyrq',

}


def handle_data(img_file):
    data_list = ocr_img(img_file)
    data = {}
    for d in data_list:
        try:
            a = d.split(':')[0]
            b = d.split(':')[1]
            a = syllable[a]
            data[a] = b
        except:
            pass
    return data


def last_data(username):
    for _ in range(5):
        try:
            f = os.getcwd()
            file1 = os.path.join(f, 'img')
            file2 = os.path.join(file1, str(username))
            file_list = os.listdir(file2)
            data = []
            i = 1
            j = 1
            for file in file_list:
                if 'xj.' in file:
                    title = file.split('_')[0]
                    lq_f = str(title) + '_xjlq.png'
                    by_f = str(title) + '_xjby.png'
                    lq = imageToStr(os.path.join(file2, lq_f))
                    by = imageToStr(os.path.join(file2, by_f))
                    xj = {}
                    xj_data = handle_data(os.path.join(file2, file))
                    xj_data['lq_pic'] = lq
                    xj_data['by_pic'] = by
                    a = file.split('_')[0]
                    b = 'xj_' + str(i)
                    i += 1
                    xj[b] = a
                    xj['xj_data'] = xj_data
                    data.append(xj)
                elif 'xl.' in file:
                    title = file.split('_')[0]
                    xl_f = str(title) + '_xlzs.png'
                    xlzs = imageToStr(os.path.join(file2, xl_f))
                    xl = {}
                    xl_data = handle_data(os.path.join(file2, file))
                    xl_data['xl_pic'] = xlzs
                    a = file.split('_')[0]
                    b = 'xl_' + str(j)
                    j += 1
                    xl[b] = a
                    xl['xj_data'] = xl_data
                    data.append(xl)
                else:
                    pass
            return data
        except Exception as e:
            print(e)


def imageToStr(image):
    with open(image, 'rb') as f:
        image_byte = base64.b64encode(f.read())
    image_str = image_byte.decode('ascii')  # byte类型转换为str
    return image_str


if __name__ == '__main__':
    data = last_data('手机号')
    print(data)
