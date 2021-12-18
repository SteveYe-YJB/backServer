import pandas as pd

# 随机码


class CalculationTool:
    # 生成指定长度的随机编码
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
