from email import message
from flask import Blueprint
from flask_mail import Message
from App.utils.ext import mail

email = Blueprint('email', __name__, url_prefix='/api/email')

@email.route('/test')
def my_mail():
    message = Message(
        subject= '测试邮箱', # 主题
        recipients= ['790021919@qq.com', '1071354998@qq.com'], # 收件人
        body= '这是一封测试邮件', # 正文
        html= '' # 富文本内容
    )
    mail.send(message)
    return '发送成功'
