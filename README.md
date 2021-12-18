# 注意

## 配置环境包

- 生成项目依赖文件 pip freeze > requirements.txt

- 安装依赖文件 pip install -r requirements.txt

## 开启服务

- 本地

  - python manage.py runserver -h localhost -p 8000 -d -r --thread 开启服务

- 生产 linux

  - nohup python manage.py runserver -h localhost -p 8000 -d -r --thread >/dev/null 2>&1 & 不阻塞进程运行

## 数据库操作

- 配置数据库指令

  - python manage.py db init # 创建储存记录,第一次需要执行

  - python manage.py db migrate # 创建迁移

  - python manage.py db upgrade # 提交迁移

  - python manage.py db downgrade # 回退上一个提交迁移

- 换电脑迁移时

  1. 确保数据库没有 models 无相关的表，有则备份

  2. 删除数据库中的 alembic_version 表

  3. 删除 migrations 文件夹

  4. 重新执行 init,migrate,upgrade 命令

- 导入数据库已有的表格

  - pip install flask-sqlacodegen

  - flask-sqlacodegen --flask --outfile <输出的文件名> <数据库连接 URI> 会自动生成一个文件是已有表格的模型对应表

  - 还要重新修改一下，比如表之间的关系,外键之类的，一对多,多对一
