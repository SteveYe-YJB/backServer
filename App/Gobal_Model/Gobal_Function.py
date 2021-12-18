# -*- coding: utf-8 -*-

from random import sample
import os
import shutil
from pathlib import Path
from time import time
import hmac
import base64
from Function_DateTime import Date

# 随机码


class CodeId:
    # 生成指定长度的随机编码
    def RandCode(self, length):
        '''
            :param length: integer。输出编码长度
            :return: 生成后的指定长度的随机编码
        '''
        result = ''.join(
            sample(
                'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890',
                length
            )
        )
        return result

    # 生成35位带时间戳的KeyID
    def KeyId35(self, title='@@@@@@'):
        '''
            :param title: string。默认为@@@@@@, 支持六位指定编码
            :return: 生成35位带日期时间格式的数据库主键编码。结构 6位自定义识别码 + 20位日期时间编码 + 9位随机码
        '''
        timeStamp = '{0:020d}'.format(
            int(
                Date.DateTimeFormat(
                    self=None,
                    dateTime=None,
                    formatStr='%Y%m%d%H%M%S%f',
                    cutCount=0
                )
            )
        )
        result = '{}{}{}'.format(
            title[0:6],
            timeStamp,
            CodeId.RandCode(
                self=None,
                length=9
            )
        )
        return result

    # 元组转换
    def GetTuple(self, data):
        resultTuple = ()
        if isinstance(data, str):
            resultTuple = "('" + data + "')"
        elif len(data) > 1:
            resultTuple = tuple(data)
        elif len(data) == 1:
            resultTuple = "('" + data[0] + "')"
        return resultTuple

    # 把一个文件夹下的文件移动到另外一个文件夹
    def remove_file(self, old_path, new_path, fileName):
        # print(old_path)
        # filelist = os.listdir(old_path) #列出该目录下的所有文件,listdir返回的文件列表是不包含路径的。
        # print(111111)
        # for file in filelist:
        src = os.path.join(old_path, fileName)
        dst = os.path.join(new_path, fileName)
        shutil.move(src, dst)

    # 根据表名检验是否存在此文件夹并返回路径
    def CheckSheetName(self, new_path, fileName):
        # dateDay = str(fileName.split('.')[1].split('天猫')[0])
        # dateMonth = str(fileName.split('.')[0])
        # dateYear = str(dateTimeAll.datetime.now().year)
        fileDay = fileName[0:8]
        dateMonth = str(int(fileDay[4:6]))
        dateYear = fileDay[0:4]
        new_pathFile = Path(
            new_path + '\\' + dateYear + '\\' + dateMonth + '月' + '\\' + fileName)
        new_pathMonthDir = Path(
            new_path + '\\' + dateYear + '\\' + dateMonth + '月')
        new_pathYearDir = Path(new_path + '\\' + dateYear)
        dir_MonthPath = new_pathMonthDir.exists()
        dir_YearPath = new_pathYearDir.exists()
        file_path = new_pathFile.exists()
        #
        if dir_YearPath == False:
            os.makedirs(new_path + '\\' + dateYear)

        if dir_MonthPath == False:
            os.makedirs(new_path + '\\' + dateYear +
                        '\\' + dateMonth + '月')

        if file_path:
            # dst = ''
            # src = os.path.join(new_path + '\\' + dateYear + '\\' + dateMonth + '月' , fileName)
            # if '京东' in fileName:
            #     dst = os.path.join(Config_FileName.RMOVEFILE_JDNOTNEED, fileName)
            # elif '天猫' in fileName:
            #     dst = os.path.join(Config_FileName.RMOVEFILE_TMALLNOTNEED, fileName)
            # shutil.move(src, dst)
            return {'fileState': False, 'filePath': ''}

        return {'fileState': True, 'filePath': new_path + '\\' + dateYear + '\\' + dateMonth + '月'}

    # 生成token
    def generate_token(self, key, expire=3600):
        ts_str = str(time.time() + expire)
        ts_byte = ts_str.encode("utf-8")
        sha1_tshexstr = hmac.new(
            key.encode("utf-8"), ts_byte, 'sha1').hexdigest()
        token = ts_str+':'+sha1_tshexstr
        b64_token = base64.urlsafe_b64encode(token.encode("utf-8"))
        return b64_token.decode("utf-8")

    # 验证token
    def certify_token(self, key, token):
        token_str = base64.urlsafe_b64decode(token).decode('utf-8')
        token_list = token_str.split(':')
        if len(token_list) != 2:
            return False
        ts_str = token_list[0]
        if float(ts_str) < time.time():
            # token expired
            return False
        known_sha1_tsstr = token_list[1]
        sha1 = hmac.new(key.encode(
            "utf-8"), ts_str.encode('utf-8'), 'sha1')
        calc_sha1_tsstr = sha1.hexdigest()
        if calc_sha1_tsstr != known_sha1_tsstr:
            # token certification failed
            return False
        # token certification success
        return True
