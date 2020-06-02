#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/5/21 10:46
# @Author : xjm
# @Site : 
# @File : user_test.py
# @Software: PyCharm
from unittest import TestCase
from dao import user_dao
from settings import encryption
import requests

dao = user_dao.UserDao()


class TestUser(TestCase):

    def test_save(self):

        user = {
            'username': 'xjm1',
            'password': '123456',
            'email': '1@2.com',
            'sex': 'female'
        }

        result = dao.register(**user)

        print(result)

        self.assertEqual(result['status'], 200, "请求失败")

    def test_login(self):

        user, resp = dao.login("xjm", "000000")

        print(user, resp)

        self.assertEqual(resp['status'], 200, "请求失败")

    def test_login_request(self):

        data = {
            'username': 'xjm',
            'password': '000000'
        }

        resp = requests.post("http://localhost:5000/user/login", data=data)

        print(resp.json())

        self.assertEqual(resp.json()['code'], 200, '请求失败')

    def test_logout_request(self):

        resp = requests.get("http://localhost:5000/user/logout")

        print(resp.text)