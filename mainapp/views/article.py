from flask import Blueprint, request,render_template, redirect, jsonify, session
from dao import article_dao
from mainapp.views import comment

blue = Blueprint('articleBlue', __name__)

dao = article_dao.ArticleDao()


@blue.route('/all', methods=['GET'])
def article_list():
    articles, result = dao.search_all()
    return jsonify(articles)


@blue.route('/<int:aid>', methods=['GET'])
def article_aid(aid):
    comments, _ = comment.aid_comments(aid)
    articles, _ = dao.search_all()
    article, result = dao.search(aid)
    if session.get('login_user'):  # 验证用户是否登录
        user = session.get('login_user')[0]
        return render_template("blog.html", articles=articles, article=article[0],
                               user=user, comments=comments, len_c=len(comments))
    return render_template("blog.html", articles=articles, article=article[0], comments=comments, len_c=len(comments))


@blue.route('/<int:page>/<int:num>', methods=['GET'])
def page(page, num):
    articles, result = dao.search_page((page-1)*num, num)
    article_num = len(dao.search_all()[0])
    pages = article_num // num if article_num % num == 0 else article_num // num + 1
    index = []
    for i in range(1, pages + 1):
        index.append(pages - i + 1)
    if not session.get('login_user'):  # 验证用户是否登录
        if articles:
            return render_template('index.html', articles=articles[0])
        return render_template('index.html', articles=[])
    user = session.get('login_user')[0]
    return render_template('index.html', user=user, articles=articles, index=index, pages=pages, num=num, page=page)


def article_page(page, num):
    articles, result = dao.search_page((page-1)*num, num)
    article_num = len(dao.search_all()[0])
    page = article_num // num if article_num % num == 0 else article_num // num + 1
    index = []
    for i in range(1, page + 1):
        index.append(page - i + 1)
    return articles, index, len(index)


@blue.route('/click_add/<int:aid>', methods=['GET'])
def click_add(aid):

    result = dao.click_add(aid)

    return jsonify(result)

