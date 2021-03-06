from flask import request
from App.Gobal_Model.Gobal_Function import GobalFun
from App.utils.ext import cache
from .tool.Tool import tool
from .test.sql_test import sql
from .test.email import email
# 登陆模块
from .login.register import login

def init_view(app):
    
    #  在请求进入视图函数之前 做出响应
    @app.before_request
    def checkToken():
        token = request.headers.get('Authorization')
        login_key = token and cache.get(token)
        if request.path == "/api/login":
            return None
        elif not token or (not login_key or not GobalFun.certify_token(login_key, token)) :
            return {
                'state': 421,
                'msg': '会话过期,请重新登陆!',
                'data': {}
            }
        return None

    app.register_blueprint(tool)
    app.register_blueprint(sql)
    app.register_blueprint(email)
    app.register_blueprint(login)
