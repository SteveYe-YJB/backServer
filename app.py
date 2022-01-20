#coding:utf-8
import os
from pathlib import Path
from App import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
from dotenv import load_dotenv, find_dotenv

# 加载.env中的所有环境变量,自动识别根目录.env文件
load_dotenv(find_dotenv())

# 动态识别该代码所在电脑是开发者还是生产环境还是其他
env = os.environ.get('FLASK_ENV', 'develop')
app = create_app(env)

# 集成数据库
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
