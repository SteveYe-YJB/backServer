from flask import Blueprint, jsonify, request
from App.models.common.request import RequestTool
from App.models.Login.LoginTool import LoginTool

login = Blueprint('login', __name__, url_prefix='/api/login')

# 注册
@login.route('/register', methods=['POST'])
def user_login():   
   # 初始化返回数据
   result = {
      'state': '0',
      'msg': '',
      'data': {}
   }
   # 上送字段
   fileDict = {
      'account_no': 'accountNo',  # 用户名称
      'pass_word': 'passWord' # 用户查看密码
   }
   requestData = RequestTool.RequestData(fileDict)
   if bool(requestData['accountNo']) and bool(requestData['passWord']) :
      result['data'] = LoginTool.Register(requestData, request.headers.get('Authorization'))
      if not bool(result['data']):
         result['msg'] = '密码错误'
      else:
         result['state'] = '1'
         result['msg'] = '登陆成功'
   else: 
      result['msg'] = '密码或账号不符合要求'
   return jsonify(result)
