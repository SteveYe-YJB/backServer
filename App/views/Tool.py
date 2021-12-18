from flask import request, Blueprint, jsonify
from App.models.calculationTool import CalculationTool

tool = Blueprint('tool', __name__, url_prefix='/api')


@tool.route('/tool/standardScore', methods=['POST', 'GET'])
def toolTest():
    result = {
        'state': '0',
        'msg': '',
        'data': []
    }
    if request.method == 'POST':
        result['state'] = '1'
        print()

        if set(['score_data', 'new_std', 'new_mean']) <= set(request.json.keys()):
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
