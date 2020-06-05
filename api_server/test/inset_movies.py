#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 20/5/23 20:59
# @Author : xjm
# @Site : 
# @File : inset_movies.py
# @Software: PyCharm

import json
import pymysql
from pymysql.cursors import DictCursor

CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'port': 3306,
    'password': '123456',
    'db': 'film_tickets',
    'charset': 'utf8',
    'cursorclass': DictCursor  # 查询结果以字典形式显示
}


class DB(object):
    def __init__(self):
        self.conn = pymysql.Connect(**CONFIG)

    def __enter__(self):
        return self.conn.cursor()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:  # 有异常
            print(exc_type)
            self.conn.rollback()
        else:
            self.conn.commit()

    def close(self):
        if self.conn:
            self.conn.close()
            self.conn = None


class Dao(object):
    def __init__(self):
        self.db = DB()

    def info_save(self, table, **data):

        sql = "insert into %s(%s) values(%s)"
        a_names = ",".join([key for key in data])
        a_placeholders = ",".join(['%%(%s)s' % key for key in data])
        with self.db as c:
            c.execute(sql % (table, a_names, a_placeholders), data)
            if c.rowcount > 0:
                return {'status': 200, 'msg': 'success'}
        return {'status': 404, 'msg': 'fail'}


if __name__ == '__main__':

    dao = Dao()

    movies = []

    with open("movie.txt", 'r') as fp:
        for i in fp:
            movies.append(json.loads(i.strip()))

    for item in movies:
        print(dao.info_save('movies', **item))