from app import app  # 当定时任务需要调用数据库时引用
# 定义任务执行程序h


def print_job():
    print("I'm a scheduler!")
