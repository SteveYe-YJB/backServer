# excel处理类
import pandas as pd

class ExcelTool:
    # 获取excel数据
    def GetExcelData(filePath, fileType='excel', sheet_name=''):
        '''
            :filePath 文件路径
            :fileType 文件类型
        '''
        excelData = pd.DataFrame()
        if fileType == 'excel':
            # 读取excel数据
            excelData = pd.read_excel(filePath,sheet_name)
        return excelData
