from settings import encryption
import pymysql
from pymysql.cursors import DictCursor


CONFIG = {
    'host': '127.0.0.1',
    'user': 'root',
    'port': 3306,
    'password': '123456',
    'db': 'api_server',
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


class BaseDao(object):
    def __init__(self):
        self.db = DB()

    def find_all(self, table, where=None, *where_args):
        sql = "select * from %s" % table
        if where:
            sql += where

        with self.db as c:
            c.execute(sql, where_args)
            result = list(c.fetchall())
            if result:
                response = {'status': 200, 'msg': 'success'}
            else:
                response = {'status': 404, 'msg': 'fail'}
            return result, response

    def del_one(self, table, _id):
        sql = "delete from %s where id=%s" % (table, _id)
        with self.db as c:
            c.execute(sql)
            if c.rowcount > 0:
                return {'status': 200, 'msg': 'success'}
        return {'status': 404, 'msg': 'fail'}

    def user_save(self, table, **data):

        user, resp = self.find_all(table, ' where username=%s', data['username'])

        if not user:
            sql = "insert into %s(%s) values(%s)"
            col_names = ",".join([key for key in data])
            col_placeholders = ",".join(['%%(%s)s' % key for key in data])
            with self.db as c:
                c.execute(sql % (table, col_names, col_placeholders), data)
                if c.rowcount > 0:
                    return {'status': 200, 'msg': 'success'}
        return {'status': 404, 'msg': 'fail'}

    def info_save(self, table, **data):
        sql = "insert into %s(%s) values(%s)"
        a_names = ",".join([key for key in data])
        a_placeholders = ",".join(['%%(%s)s' % key for key in data])
        with self.db as c:
            c.execute(sql % (table, a_names, a_placeholders), data)
            if c.rowcount > 0:
                return {'status': 200, 'msg': 'success'}
        return {'status': 404, 'msg': 'fail'}

    def update(self, table, _id, **data):
        sql = "update %s set %s where aid = %s"
        update_cols = ",".join(["%s=%%(%s)s" % (key, key) for key in data])
        with self.db as c:
            c.execute(sql % (table, update_cols, _id), data)
            if c.rowcount > 0:
                return {'status': 200, 'msg': 'success'}
        return {'status': 404, 'msg': 'fail'}


if __name__ == '__main__':
    dao = BaseDao()
    pwd = encryption('000000')
    r = dao.find_all('users',
                     'where username=%s and password=%s',
                     'xjm', pwd)
    print(r)
    # result = dao.insert("w12s3", "123456", "眉山", "女")
    # print(result)

    # data = {
    #     'username': 'wsy',
    #     'password': encryption('000000'),
    #     'email': '1@2.com',
    #     'sex': 'female'
    # }
    #
    # result = dao.user_save('users', **data)
    #
    # print(result)