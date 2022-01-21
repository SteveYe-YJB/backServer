# 第三方插件
from flask_caching import Cache
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_apscheduler import APScheduler
from flask_session import Session
from flask_cors import CORS
from flask_mail import Mail

# 多线程
import platform
import atexit

# 实例化各种工具
cache = Cache(config={
    'CACHE_TYPE': 'redis'
})
db = SQLAlchemy()
migrate = Migrate()
scheduler = APScheduler()
mail = Mail()

# 把工具绑定到App上
def init_ext(app):
    db.init_app(app)  # 操作数据库
    migrate.init_app(app, db)  # 管理迁移数据库
    Session(app)
    cache.init_app(app) # 启动缓存
    CORS(app, supports_credentials=True) # 跨域问题
    # 配置任务，不然无法启动任务
    scheduler_init(app)  # 定时任务
    # 配置邮箱,邮箱配置参数在配置文件中
    mail.init_app(app)

# 启动文件锁,防止重复运行定时任务


def scheduler_init(app):
    """
    保证系统只启动一次定时任务
    :param app:
    :return:
    """
    if platform.system() != 'Windows':
        fcntl = __import__("fcntl")
        f = open('scheduler.lock', 'wb')
        try:
            # print(11111)
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug('Scheduler Started,---------------')
        except:
            pass

        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()

        atexit.register(unlock)
    else:
        msvcrt = __import__('msvcrt')
        f = open('scheduler.lock', 'wb')
        try:
            # print(2222)
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug('Scheduler Started,----------------')
        except:
            pass

        def _unlock_file():
            try:
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except:
                pass

        atexit.register(_unlock_file)
