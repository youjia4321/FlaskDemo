#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/5/21 10:47
# @Author : xjm
# @Site : 
# @File : article_test.py
# @Software: PyCharm

from dao import article_dao
from unittest import TestCase
from datetime import datetime

dao = article_dao.ArticleDao()


class TestArticle(TestCase):
    def test_save(self):
        data = {
            'title': '基于python的网络爬虫',
            'author': '向佳明',
            'add_time': datetime.now(),
            'content': '稍后会再次更新...'
        }
        result = dao.save(**data)
        self.assertEqual(result['status'], 200, '请求失败')

    def test_search(self):
        articles, result = dao.search(2)
        print(articles)
        self.assertEqual(result['status'], 200, '请求失败')

    def test_search_all(self):
        articles, result = dao.search_all()
        print(articles)
        self.assertEqual(result['status'], 200, '请求失败')

    def test_click(self):

        result = dao.click_add(2)

        self.assertEqual(result['status'], 200, '请求失败')

    def test_page(self):

        articles, result = dao.search_page(0, 3)

        print(articles)

        self.assertEqual(result['status'], 200, '请求失败')