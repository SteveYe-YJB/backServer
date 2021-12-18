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


class Config():
    DEBUG: False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SESSION_TYPE = 'redis'  # session指定redis
    SESSION_PERMANENT = False  # 如果设置session的生命周期是否是会话期, 为True，则关闭浏览器session就失效
    SESSION_USE_SIGNER = False  # 是否对发送到浏览器上session的cookie值进行加密
    SESSION_KEY_PREFIX = "session:"  # 保存到redis的session数的名称前缀
    # session保存数据到redis时启用的链接对象
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port='6379')  # 用于连接redis的配置
    SQLALCHEMY_POOL_SIZE = 5  # 数据库连接池的大小。默认是数据库引擎的默认值(通常是 5)。


class DevelopConfig(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'mysqldb',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'database_local_test_YJB_20211013',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class TestConfig(Config):
    DEBUG = True
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'mysqldb',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'database_local_test_YJB_20211013',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class StagingConfig(Config):
    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'mysqldb',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'database_local_test_YJB_20211013',
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


class ProductConfig(Config):

    dbinfo = {
        'ENGINE': 'mysql',
        'DRIVER': 'mysqldb',
        'USER': 'root',
        'PASSWORD': '794652asd',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'database_local_test_YJB_20211013',
        # 'DSNNAME': 'SQLSERVER11'
        # 'DSNNAME': 'SALEDATE'
        # 'DSNNAME': 'SALEDATE20201126'
    }
    SQLALCHEMY_DATABASE_URI = get_db_url(dbinfo)


envs = {
    'develop': DevelopConfig,
    'testing': TestConfig,
    'staging': StagingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}
