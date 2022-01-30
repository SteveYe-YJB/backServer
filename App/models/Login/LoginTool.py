from App.DB_Module import UserInfomodel,UserLoginModel
from App.utils.ext import db, cache
from App.models.common.crypt import Crypt
from datetime import datetime
from App.Gobal_Model.Gobal_Function import GobalFun

class LoginTool:
    # 计算转换后的方差
    def Register(data, oldToken): 
        login_id = ''
        result = {}
        # 查询是否存在用户
        userInfo = UserInfomodel().getUserInfo(
            account_no= data['accountNo']
        ).first()

        if not userInfo is None and Crypt.Encrypt(data['passWord']) == userInfo.password:
            # 根据user_id获取login_key_id
            user_login = db.session.query(UserLoginModel).filter_by(user_id = userInfo.user_id)
            login_id = user_login.first().login_key_id
            user_name = userInfo.user_name
            user_login.update({
                'update_time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            })
            # 提交数据库改变数据
            db.session.commit()
            
            # 生成token
            token = GobalFun.generate_token(login_id)
            # 删除redis旧token
            oldToken and cache.delete(oldToken)
            # 设置新token
            cache.set(token, login_id)

            result = {
                'token': token,
                'accountNo': data['accountNo'],
                'userName': user_name
            }

        return result
    


        # if userInfo is None:
        #     # 暂无用户,需新增
        #     user_id = Crypt.Encrypt(data)
        #     login_id = Crypt.Encrypt(user_id)
        #     UserInfomodel.insertUserInfo(
        #         user_id = user_id,
        #         user_name = '',
        #         account_no = data['accountNo'],
        #         password = Crypt.Encrypt(data['passWord'])
        #     )
        #     UserLoginModel.insertUserLogin(
        #         login_key_id= login_id,
        #         user_id = user_id
        #     )