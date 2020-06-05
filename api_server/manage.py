from mainapp import app
from flask_script import Manager, Server
from flask_cors import CORS
from flask import url_for, redirect, session
from mainapp.views import user, article, comment


@app.route("/", methods=['GET'])
def index():
    return redirect(url_for('userBlue.index'))


# 已脚本的方式启动
if __name__ == '__main__':
    # 解决跨域问题
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

    app.register_blueprint(user.blue, url_prefix='/user')
    app.register_blueprint(article.blue, url_prefix='/article')
    app.register_blueprint(comment.blue, url_prefix='/comment')

    manager = Manager(app)
    # 启动debug模式
    manager.add_command("runserver", Server(use_debugger=True))
    manager.run()

# 启动命令：跟django框架启动命令差不多
# python xxx.py runserver -h host -p port
