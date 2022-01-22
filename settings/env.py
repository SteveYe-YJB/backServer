# 迁移电脑的时候：
# 1. SQLSERVER
# 1.1 确保迁移的电脑DSNNAME设置一致
# SQLSERVER配置参数
# {
#     'ENGINE': 'mssql',
#     'DRIVER': 'pyodbc',
#     'USER': 'sa',
#     'PASSWORD': 'huiwei.2019',
#     'HOST': '172.16.16.231',
#     'PORT': '3306',
#     'NAME': 'database_local_test_YJB_20200827',
#     'DSNNAME': 'SQLSERVER11'
#     # 'DSNNAME': 'SALEDATE'
#     # 'DSNNAME': 'SALEDATE20201126'
# }
import redis
from environs import Env

env = Env()
env.read_env()  # read .env file, if it exists
print(env('MAIL_PASSWORD', ''))
# import os
# from dotenv import load_dotenv, find_dotenv
# 加载.env中的所有环境变量,自动识别根目录.env文件
# load_dotenv(find_dotenv())

# 动态识别该代码所在电脑是开发者还是生产环境还是其他
# env = os.environ.get('FLASK_ENV', 'develop')

# 公共配置参数类
class Config():
    DEBUG: False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False # 是否跟踪每次的修改
    SESSION_TYPE = 'redis'  # session指定redis
    SESSION_PERMANENT = False  # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = "session:"  # 保存到redis的session数的名称前缀
    # session保存数据到redis时启用的链接对象
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置
    SQLALCHEMY_POOL_SIZE = 5  # 数据库连接池的大小。默认是数据库引擎的默认值(通常是 5)。
    JSON_AS_ASCII = False # 返回报文中文乱码
    CACHE_DEFAULT_TIMEOUT = 60*3 # 缓存保留时间,单位为分钟
    # 邮件参数
    MAIL_SERVER = env('MAIL_SERVER', '') # 邮箱服务地址
    MAIL_PORT = env('MAIL_PORT', -1) # 邮箱端口
    MAIL_USE_TLS = env.bool('MAIL_USE_TLS', '')
    MAIL_USE_SSL = env.bool('MAIL_USE_SSL', '')
    MAIL_DEBUG = env.bool('MAIL_DEBUG', '')
    MAIL_USERNAME = env('MAIL_USERNAME', '') # 邮箱地址
    MAIL_PASSWORD = env('MAIL_PASSWORD', '') # # 该参数需要到qq邮箱 -》设置 -》账号设置 -》开启POP3/SMTP服务 -》 获取密码
    MAIL_DEFAULT_SENDER = env('MAIL_DEFAULT_SENDER', '') # 同邮箱地址


def get_db_url(dbinfo):
    ENGINE = dbinfo.get('ENGINE')
    DRIVER = dbinfo.get('DRIVER')
    USER = dbinfo.get('USER')
    PASSWORD = dbinfo.get('PASSWORD')

    # DSNNAME = dbinfo.get('DSNNAME') # sqlserver
    # return '{}+{}://{}:{}@{}'.format(ENGINE,DRIVER,USER,PASSWORD,DSNNAME) # sqlserver 配置

    HOST = dbinfo.get('HOST')  # mysql
    PORT = dbinfo.get('PORT')  # mysql
    NAME = dbinfo.get('NAME')  # mysql
    # mysql配置
    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)

class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE': 'mysql',
        # 'DRIVER': 'mysqldb',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'ry_flask',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class TestConfig(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE': 'mysql',
        # 'DRIVER': 'mysqldb',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'ry_flask',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        # 'DRIVER': 'mysqldb',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'ry_flask',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class ProductConfig(Config):

    dbinfo = {
        'ENGINE': 'mysql',
        # 'DRIVER': 'mysqldb',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'ry_flask',
        # 'DSNNAME': 'SQLSERVER11'
        # 'DSNNAME': 'SALEDATE'
        # 'DSNNAME': 'SALEDATE20201126'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)

def getEnv():
    envs = {
        'develop': DevelopConfig,
        'testing': TestConfig,
        'staging': StagingConfig,
        'product': ProductConfig,
        'default': DevelopConfig
    }
    return envs.get(env('FLASK_ENV', 'develop'))
