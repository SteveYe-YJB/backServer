from flask import request, Blueprint, jsonify
from App.models.calculationTool import CalculationTool
from App.models.common.request import RequestTool

tool = Blueprint('tool', __name__, url_prefix='/api/tool')


@tool.route('/standardScore', methods=['POST', 'GET'])
def standardScore():
    result = {
        'state': '0',
        'msg': '',
        'data': []
    }
    if request.method == 'POST':
        result['state'] = '1'
        if set(['score_data', 'new_std', 'new_mean']) <= set(request.json.keys()) and bool(request.json.get('score_data')):
            result['data'] = CalculationTool.StandardScore(
                request.json.get('score_data'),
                request.json.get('new_std'),
                request.json.get('new_mean'))
        else:
            result['msg'] = '上送参数不齐'
        return jsonify(result)
    else:
        result['msg'] = '无效的get请求方式'
        return jsonify(result)

@tool.route('/readProject', methods=['POST', 'GET'])
def readProject():
    # 初始化返回函数
    result = {
        'state': '0',
        'msg': '',
        'data': []
    }
    # 上送字段
    fileDict = {
        'user_name': 'userName',  # 用户名称
        'pass_word': 'passWord' # 用户查看密码
    }
    if request.method == 'POST':
        requestData = RequestTool.RequestData(fileDict)
        result['data'] = CalculationTool.GetExcelList(requestData, 'App/static/files/2020科研数据.xlsx', '横向到帐经费')
        result['state'] = '1'
        return result
    else:
        result['msg'] = '无效的get请求方式'
        return result