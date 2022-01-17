import pandas as pd
from .common.excel import ExcelTool
# 业务


class CalculationTool:
    # 计算转换后的方差
    def StandardScore(data, std, mean):
        '''
            :data 转换的数据列表
            :std 转换后的标准差
            :mean 转换后的均值
        '''

        dataFrame = pd.DataFrame(data)
        dataFrame['z-score'] = (dataFrame['score'] -
                                dataFrame.score.mean()) / dataFrame.score.std()

        dataFrame['change_std_score'] = dataFrame['z-score'] * std

        dataFrame['change_score'] = dataFrame['change_std_score'] + mean

        return dataFrame.to_dict(orient='records')

    # 返回查看excel的项目列表
    def GetExcelList(data, filePath, sheet_name):
        '''
          :data 请求数据
          :filePath 文件路径
          :sheet_name excel工作表名称
        '''
        # 读取excel数据
        excelData = ExcelTool.GetExcelData(filePath, sheet_name=sheet_name)
        # 改变列名
        if len(excelData) > 0:
            excelData.rename(columns={
                '合同编号': 'contractNo',
                '项目名称': 'projectName',
                '合作单位': 'partner',
                '合作单位所属地址': 'companyAddress',
                '项目负责人': 'projectLeader',
                '所属单位': 'company',
                '来款单位': 'payer',
                '来款时间': 'paymentTime',
                '金额/元': 'amount',
                '办理入账时间': 'entryTime'
            }, inplace=True)
            excelData['amount'] = excelData['amount'].astype(str)
            print(excelData)
            # 根据条件筛选
                # 超级管理员密码则全部返回
                # 有姓名且不是超级管理员密码则根据姓名筛选
            if data['userName'].strip() and data['passWord'] != '123456':
                excelData = excelData[(excelData['projectLeader'] == data['userName'])]
            return excelData.to_dict(orient='records')
        else:
            return []