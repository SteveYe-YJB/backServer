#coding:utf-8
import os
from App import create_app
from dotenv import load_dotenv, find_dotenv
from flask_script import Manager
from flask_migrate import MigrateCommand

# 加载.env中的所有环境变量,自动识别根目录.env文件
load_dotenv(find_dotenv())

# 动态识别该代码所在电脑是开发者还是生产环境还是其他
env = os.environ.get('FLASK_ENV', 'develop')

# 集成创建app
app = create_app(env)

# 集成数据库Migrate管控
manage = Manager(app)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(
        host='localhost',
        port= 9528,
        debug=True
    )
