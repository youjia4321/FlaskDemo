from flask import Flask, render_template
from flask_session import Session

import settings

# 默认的static_folder是static
app = Flask(__name__, static_folder='static', static_url_path='/s')

# 从指定的对象加载Flask服务的配置
app.config.from_object(settings.Dev)


# 自定义过滤器
@app.template_filter("date_format")
def date_filter(value, *args):
    return value.strftime(args[0])


@app.template_filter("length_format")
def str_filter(value, *args):
    return value[: 60]


@app.errorhandler(404)
def not_found(error):
    return render_template("404.html")


# @app.errorhandler(Exception)
# def server_exception(error):
#     return render_template("500.html")
#
#
# @app.errorhandler(500)
# def server_500(error):
#     return render_template("500.html")
