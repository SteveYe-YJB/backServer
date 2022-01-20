from flask import Flask
from App.timerTasks.timerTasks import TimeTasks
from App.utils.ext import init_ext
from App.views import init_view
from settings.env import envs


def create_app(env):
    app = Flask(__name__)

    # 配置数据库
    app.config.from_object(envs.get(env))

    # 配置定时任务
    app.config.from_object(TimeTasks())

    # 初始化第三方拓展库
    init_ext(app)

    # 实例路由
    init_view(app)
    return app
