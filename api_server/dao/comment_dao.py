from dao import BaseDao


class CommentDao(BaseDao):

    def find_by_aid(self, aid):
        """

        :param aid: 文章id
        :return: 该文章的所有评论信息
        """
        return super().find_all('comments', ' where aid=%s', aid)

    def save(self, **data):
        """

        :param data: 字典形式的评论对象
        :return: 响应码
        """
        return super().info_save('comments', **data)
