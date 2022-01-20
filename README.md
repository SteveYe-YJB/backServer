# 注意

## 配置环境包

- 生成项目依赖文件 pip freeze > requirements.txt

- 安装依赖文件 pip install -r requirements.txt

- 特许包版本
  - pip3 install flask_migrate==2.7.0
  - pip install python-dotenv
  
## 开启服务

- 本地

  - python app.py runserver -h localhost -p 9528 -d -r --thread 开启服务

- 生产 linux

  - nohup python app.py runserver -h localhost -p 9528 -d -r --thread >/dev/null 2>&1 & 不阻塞进程运行

## 数据库操作

- 配置数据库指令

  - flask db init # 创建储存记录,第一次需要执行

  - flask db migrate # 创建迁移

  - flask db upgrade # 提交迁移

  - flask db downgrade # 回退上一个提交迁移

- 换电脑迁移时

  1. 确保数据库没有 models 无相关的表，有则备份

  2. 删除数据库中的 alembic_version 表

  3. 删除 migrations 文件夹

  4. 重新执行 init,migrate,upgrade 命令

- 导入数据库已有的表格

  - pip install flask-sqlacodegen

  - flask-sqlacodegen --flask --outfile <输出的文件名> <数据库连接 URI> 会自动生成一个文件是已有表格的模型对应表

  - 还要重新修改一下，比如表之间的关系,外键之类的，一对多,多对一

- 数据库的配置以及常见用法
  - 数据库配置事例
    ```
      class Customer(db.Model):
        __tablename__= "customer"
        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String(16))

      class Address(db.Model):
          __tablename__= "adress" # 表名
          id = db.Column(db.Integer, primary_key = True)
          position = db.Column(db.String(128))
          custom_id = db.Column(db.Integer, db.ForeignKey(Customer.id)) #  创建Customer外键

          customer = db.relationship('Customer', backref = 'address') # 一对多,一个customer对应多个address

      class CustomerDetail(db.Model):
          __tablename__= "customerDetail"
          id = db.Column(db.Integer, primary_key = True)
          height = db.Column(db.Integer)
          custom_id = db.Column(db.Integer, db.ForeignKey(Customer.id)) #  创建Customer外键

          customer = db.relationship('Customer', backref = db.backref('CustomerDetail',uselist=False)) # 一对一,一个customer对应一个CustomerDetail
    ```
  - 常见操作
    ```
      # 数据库查询功能说明  

      # 外键的使用以及一对多查询
      # 创建一个Customer
      customer = Customer(name='yjb')

      # 创建一个Address
      address = Address(position = '170')

      # 关联外建
      address.customer=customer
      db.session.add(address)
      db.session.commit()

      # 获取customer对应的address，一对多查询
      print(customer.address) 

      # 一对一查询
      # 创建一个Customer
      customer = Customer.query.filter_by(id=3).first()
      # 创建一个CustomerDetail
      customerDetail = CustomerDetail(height=188)
      # 关联外建
      # customerDetail.customer=customer
      customer.CustomerDetail = customerDetail

      db.session.add(customer)
      db.session.commit()

      # 获取customer对应的address，一对一查询
      # 重复插入是旧的记录的外键会变为null,对应的外键给到新纪录
      print(customer.CustomerDetail) 
    ```

## 自动化部署

- 查看当前的版本 git tag(若报错 tag 找不到,升级 git 版本)
- 添加新的版本 git tag v0.1.0
- 推送开始自动化 git push origin v0.1.0

