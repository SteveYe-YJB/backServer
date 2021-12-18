import os
from pathlib import Path
from App import create_app
from flask_script import Manager
from flask_migrate import MigrateCommand
from dotenv import load_dotenv, find_dotenv

BASE_DIR = Path(__file__).absolute().parent

# 下面两种方法都可以拼接路径
env_path = Path(BASE_DIR).joinpath(".env")
env_path = os.path.join(BASE_DIR, ".env")

# 加载.env中的所有环境变量,两种方法均可
# 第一种可以自己拼接路径查找.env，第二种方法会自动查找.env
load_dotenv(env_path)
load_dotenv(find_dotenv())

# 动态识别该代码所在电脑是开发者还是生产环境还是其他
env = os.environ.get('FLASK_ENV', 'develop')
app = create_app(env)
manage = Manager(app)
manage.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manage.run()
