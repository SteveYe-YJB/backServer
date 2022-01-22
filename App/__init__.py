from flask import Flask, jsonify
from App.timerTasks.timerTasks import TimeTasks
from App.utils.ext import init_ext
from App.views import init_view
from settings.env import getEnv



def create_app():
    app = Flask(__name__)
    
    # 配置数据库以及公共参数,必须在第三方拓展库前面加载,因为有拓展库需要用到的参数
    app.config.from_object(getEnv())

    # 初始化第三方拓展库
    init_ext(app)

    # 实例路由
    init_view(app)

    # 配置定时任务
    app.config.from_object(TimeTasks())
    
    return app
