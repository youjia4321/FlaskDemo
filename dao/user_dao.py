from dao import BaseDao
from settings import encryption


class UserDao(BaseDao):

    def login(self, username, password):
        """

        :param username: 用户名
        :param password: 密码
        :return: 返回响应码 {'status': 200, 'msg': 'success'}
        """
        return super().find_all('users', ' where username=%s and password=%s', username, encryption(password))

    def register(self, **data):
        """

        :param data: 字典类型的用户信息
        :return: 返回响应码 {'status': 200, 'msg': 'success'}
        """

        data['password'] = encryption(data['password'])

        return super().user_save('users', **data)
