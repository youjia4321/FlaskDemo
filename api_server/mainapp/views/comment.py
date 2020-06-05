from datetime import datetime

from dao import comment_dao
from flask import Blueprint, request, redirect, url_for

blue = Blueprint('commentBlue', __name__)


dao = comment_dao.CommentDao()


def aid_comments(aid):

    return dao.find_by_aid(aid)


@blue.route('/<int:aid>', methods=['POST'])
def submit_comment(aid):
    name = request.form.get('name', None)
    email = request.form.get('email', None)
    message = request.form.get('message', None)

    if all((name, email, message)):
        data = {
            'aid': aid,
            'uname': name,
            'uemail': email,
            'cpub': datetime.now(),
            'content': message
        }
        dao.save(**data)
    return redirect(url_for('articleBlue.article_aid', aid=aid))
