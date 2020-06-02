#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/5/21 10:46
# @Author : xjm
# @Site : 
# @File : comments_test.py
# @Software: PyCharm
from datetime import datetime
from unittest import TestCase

from dao import comment_dao
from mainapp.views import comment


dao = comment_dao.CommentDao()


class TestComment(TestCase):

    def test_get(self):

        comments, result = comment.aid_comments(2)

        print(comments, result)

    def test_save(self):

        data = {
            'content': '我也觉得很行',
            'uname': 'wwm',
            'uemail': '1@2.com',
            'cpub': datetime.now(),
            'aid': 2
        }

        result = dao.save(**data)

        print(result)

        self.assertEqual(result['status'], 200, '请求失败')