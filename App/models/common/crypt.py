import hashlib
import json


class Crypt:
    # md5加密
    def Encrypt(data):
        if isinstance(data, dict):
            data = json.dumps(data)
        md5Value = hashlib.md5()
        md5Value.update(data.encode("utf-8"))
        return md5Value.hexdigest()
    # md5解密
    def Dncrypt():
        return 2


# # 1.md5 字符串加密
# # 说明：只能对字符串类型的数据进行md5加密
# pwd = "123456"
# encode_pwd = pwd.encode()  # 把字符串转为字节类型

# # 使用md5进行加密
# md5_pwd = hashlib.md5(encode_pwd)

# print('字符串加密后的值：',md5_pwd.hexdigest())



# # 2.对字典类型进行md5加密
# userinfo = {'username':'xiaoming'}
# str_userinfo = json.dumps(userinfo)       # 把字典类型转换为字符串类型
# print('转换后的字符串类型：',type(str_userinfo),'\n','转换后的字符串内容：',str_userinfo)
# # 对字符串进行编码
# encode_userinfo = str_userinfo.encode()   # 把字符串转为字节类型
# # 使用md5 进行加密
# md5_userinfo = hashlib.md5(encode_pwd)