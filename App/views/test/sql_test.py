from flask import Blueprint
from App.DB_Module import Customer,CustomerDetail,Address
from App.utils.ext import db

sql = Blueprint('sql', __name__, url_prefix='/api/sql')

@sql.route('/otm', methods=['POST', 'GET'])
def sqltest():
    # 外键的使用以及一对多查询
    # 创建一个Customer
    # customer = Customer(name='yjb')
    customer = Customer.query.filter_by(id=3).first()

    # 创建一个Address
    address = Address(position = '170')

    # 关联外建
    address.customer=customer
    db.session.add(address)
    db.session.commit()

    # 获取customer对应的address，一对多查询
    print(customer.address) 
    return 'ok'
    
@sql.route('/oto', methods=['POST', 'GET'])
def sqltest2():
    # 外键的使用以及一对多查询
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
    return 'ok'

# sql转pandas
# userInfo = pd.read_sql(
#             UserInfomodel().getUserInfo(
#                 account_no= data['accountNo'],
#                 password= Crypt.Encrypt(data['passWord'])
#             ).statement, 
#             db.session.bind)

