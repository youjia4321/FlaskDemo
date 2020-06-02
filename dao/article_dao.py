from dao import BaseDao


class ArticleDao(BaseDao):
    def search_page(self, page, num):
        
        return super().find_all('articles', ' limit %s, %s', page, num)

    def search_all(self):
        """

        :return: 所有文章信息
        """
        return super().find_all('articles')

    def search(self, aid):
        """

        :param aid: 文章的id
        :return: 文章信息
        """
        return super().find_all('articles', ' where aid=%s', aid)

    def save(self, **data):
        """

        :param data: 字典形式的文章对象
        :return: 响应码
        """
        return super().info_save('articles', **data)

    def click_add(self, aid):
        """

        :param aid: 文章id
        :param data: 更新内容
        :return: 响应码
        """
        articles, result = self.search(aid)

        data = {
            "aclick": int(articles[0]['aclick']) + 1
        }

        return super().update('articles', aid, **data)
