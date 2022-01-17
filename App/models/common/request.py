# 通用工具
from flask import request

class RequestTool:
    # 获取上送参数字典
    def RequestData(fileDict):
        '''
            :fileList 字段列表
        '''
        responseData = {}
        for fileKey, fileValue in fileDict.items():
            responseData[fileValue] = request.json.get(fileKey)
        return responseData
