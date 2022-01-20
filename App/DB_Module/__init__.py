from pyparsing import autoname_elements
from sqlalchemy import false
from App.utils.ext import db

# class Skukey(db.Model):
#     __tablename__ = 'skuKeyId_table_20201126'

#     skuKeyId = db.Column(db.Unicode(35), primary_key=True)
#     skuId = db.Column(db.Unicode(100), nullable=False)
#     dataState = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeoPle = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=False)
#     updateDateTime = db.Column(db.DateTime, nullable=False)
#     getforecast = db.relationship('Forecast', backref='getskukey', lazy =True)
#     getrollplan = db.relationship('RollPlan', backref='getskukey', lazy =True)
#     getskudetail = db.relationship('SkuDetail', backref='getskukey', lazy =True)
#     getskusale = db.relationship('SkuSale', backref='getskukey', lazy =True)
#     getskuscalping = db.relationship('SkuScalping', backref='getskukey', lazy =True)

# class MonthParameter(db.Model):
#     __tablename__ = 'monthParameter_table_20201126'

#     monthParameterKeyId = db.Column(db.Unicode(35), primary_key=True)
#     monthParameter = db.Column(db.Float(53), nullable=False)
#     parameterMonth = db.Column(db.Integer, nullable=False)
#     parameterYear = db.Column(db.Integer, nullable=False)
#     dataSate = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeoPle = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=False)
#     UpdateDateTime = db.Column(db.DateTime, nullable=False)
#     getdayparameter = db.relationship('DayParameter', backref='getmonthparameter', lazy =True)

# class Forecast(db.Model):
#     __tablename__ = 'forecast_table_20201205'

#     forecastKeyId = db.Column(db.Unicode(35), primary_key=True)
#     skuKeyId = db.Column(db.ForeignKey(Skukey.skuKeyId), nullable=False)
#     forecastMonth = db.Column(db.Integer, nullable=False)
#     forecastSaleNumber = db.Column(db.Unicode(20), nullable=False)
#     dataState = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeople = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=False)
#     updateDateTime = db.Column(db.DateTime, nullable=False)

#     # skuKeyId_table_20201126 = db.relationship('SkuKeyIdTable20201126', primaryjoin='ForecastTable20201205.skuKeyId == SkuKeyIdTable20201126.skuKeyId', backref='forecast_table20201205s', lazy =True)

# class RollPlan(db.Model):
#     __tablename__ = 'rollPlan_table_20201126'

#     rollPlanKeyId = db.Column(db.Unicode(35), primary_key=True)
#     skuKeyId = db.Column(db.ForeignKey(Skukey.skuKeyId), nullable=False)
#     planMonth = db.Column(db.Integer, nullable=False)
#     planTime = db.Column(db.Integer, nullable=False)
#     planCreateDate = db.Column(db.Unicode(20), nullable=False)
#     planSaleNumber = db.Column(db.Unicode(20), nullable=False)
#     dataState = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeople = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=False)
#     updateDateTime = db.Column(db.DateTime, nullable=False)

#     # skuKeyId_table_20201126 = db.relationship('SkuKeyIdTable20201126', primaryjoin='RollPlanTable20201126.skuKeyId == SkuKeyIdTable20201126.skuKeyId', backref='roll_plan_table20201126s', lazy =True)

# class SkuDetail(db.Model):
#     __tablename__ = 'skuDetailInfo_table_20201126'

#     skuDetailInfoKeyId = db.Column(db.Unicode(35), primary_key=True)
#     skuKeyId = db.Column(db.ForeignKey(Skukey.skuKeyId), nullable=False)
#     skuShopName = db.Column(db.Unicode(100), nullable=False)
#     skuplatformName = db.Column(db.Unicode(20), nullable=False)
#     skuName = db.Column(db.Unicode(256), nullable=False)
#     skuBrandName = db.Column(db.Unicode(100))
#     skuCategory = db.Column(db.Unicode(20))
#     skuModel = db.Column(db.Unicode(100))
#     skuModelDetail = db.Column(db.Unicode(100))
#     skuState = db.Column(db.Unicode(50))
#     skuFutureState = db.Column(db.Unicode(50))
#     skuPrice = db.Column(db.Float(53))
#     dataState = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeoPle = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=True)
#     UpdateDateTime = db.Column(db.DateTime, nullable=True)

#     # skuKeyId_table_20201126 = db.relationship('SkuKeyIdTable20201126', primaryjoin='SkuDetailInfoTable20201126.skuKeyId == SkuKeyIdTable20201126.skuKeyId', backref='sku_detail_info_table20201126s', lazy =True)

# class SkuSale(db.Model):
#     __tablename__ = 'skuSale_table_20201126'

#     saleKeyId = db.Column(db.Unicode(35), primary_key=True)
#     skuKeyId = db.Column(db.ForeignKey(Skukey.skuKeyId), nullable=False)
#     saleNumber = db.Column(db.Integer, nullable=False)
#     saleDate = db.Column(db.DateTime, nullable=False)
#     dataState = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeople = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=False)
#     updateDateTime = db.Column(db.DateTime, nullable=False)

#     # skuKeyId_table_20201126 = db.relationship('SkuKeyIdTable20201126', primaryjoin='SkuSaleTable20201126.skuKeyId == SkuKeyIdTable20201126.skuKeyId', backref='sku_sale_table20201126s', lazy =True)

# class SkuScalping(db.Model):
#     __tablename__ = 'skuScalping_table_20201126'

#     scalpingKeyId = db.Column(db.Unicode(35), primary_key=True)
#     skuKeyId = db.Column(db.ForeignKey('skuKeyId_table_20201126.skuKeyId'), nullable=False)
#     scalpingNumber = db.Column(db.Integer, nullable=False)
#     scalpingDate = db.Column(db.DateTime, nullable=False)
#     dataState = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeople = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=False)
#     updateDateTime = db.Column(db.DateTime, nullable=False)

#     # skuKeyId_table_20201126 = db.relationship('SkuKeyIdTable20201126', primaryjoin='SkuScalpingTable20201126.skuKeyId == SkuKeyIdTable20201126.skuKeyId', backref='sku_scalping_table20201126s', lazy = True)

# class DayParameter(db.Model):
#     __tablename__ = 'dayParameter_table_20201126'

#     dayParameterKeyId = db.Column(db.Unicode(35), primary_key=True)
#     dayParameter = db.Column(db.Numeric(18, 6), nullable=False)
#     parameterDate = db.Column(db.DateTime, nullable=False)
#     # monthParameterKeyId = db.Column(db.ForeignKey('monthParameter_table_20201126.monthParameterKeyId'), nullable=False)
#     monthParameterKeyId = db.Column(db.ForeignKey(MonthParameter.monthParameterKeyId), nullable=False)
#     dataSate = db.Column(db.Integer, nullable=False)
#     remark = db.Column(db.Unicode(150), nullable=False)
#     createPeoPle = db.Column(db.Unicode(20), nullable=False)
#     createDateTime = db.Column(db.DateTime, nullable=False)
#     updateDateTime = db.Column(db.DateTime, nullable=False)

# # class User(db.Model):
# #     __tablename__ = 'user'
# #     userId = db.Column(db.Integer, primary_key = True)
# #     userName = db.Column(db.String(16))
# #     userNumber = db.Column(db.String(16))
# #     userDes = db.Column(db.String(128), nullable = True)
# #     def save(self):
# #         db.session.add(self)
# #         db.session.commit()


# # class Student(db.Model):
# #     __tablename__ = 'student'
# #     studentId = db.Column(db.Integer, primary_key = True)
# #     studentName = db.Column(db.String(20))
# #     # studentPassword = db.Column(db.String(256))
# #     studentEmail = db.Column(db.String(256))
# #     def save(self):
# #         db.session.add(self)
# #         db.session.commit()

# # class Animal(db.Model):
# #     __abstract__ = True # 模型继承，防止下面继承的字段生成在同一个表
# #     id = db.Column(db.Integer, primary_key = True)
# #     name = db.Column(db.String(16))

# # class Dog(Animal):
# #     d_leg = db.Column(db.Integer, default = 4)

# # class Cat(Animal):
# #     c_eat = db.Column(db.String(32), default = 'fish')

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


