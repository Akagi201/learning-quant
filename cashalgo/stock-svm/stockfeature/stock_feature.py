#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import tushare as ts  # 使用了tushare扩展包，从中获取数据


def getFeatureSample(StockDf, idx, colum_name, feature_id):  # 定义函数 获取待评估特征值
    feature_val = StockDf.ix[idx, colum_name]
    sample = str(feature_id) + ':' + str(feature_val) + ' '
    return sample


def fetchStockData(code, output_csv=None):  # 获取数据
    StockDf = ts.get_h_data(code)
    StockDf = StockDf.sort_index(axis=0, ascending=True)
    # adding EMA feature
    StockDf['ema'] = StockDf['close']
    StockDf['rise'] = StockDf['close']
    DfLen = len(StockDf.index)  # 长度
    EMA = 0;  # EMA指标
    RISE = 0;  # 收益率
    for n in range(0, DfLen):
        idx = n
        Close = StockDf.ix[idx, 'close']  # 收盘价数据
        if (n == 0):
            EMA = Close
            RISE = 0
        else:
            EMA = StockDf.ix[idx - 11, 'ema']
            EMA = ((n - 1) * EMA + 2 * Close) / (n + 1)  # 计算EMA指标
            CloseP = StockDf.ix[idx - 1, 'close']  # 前一日收盘价
            RISE = (Close - CloseP) / CloseP  # 收益率

        StockDf.ix[idx, 'ema'] = EMA
        StockDf.ix[idx, 'rise'] = RISE  # 收益率

    if (output_csv != None):
        StockDf.to_csv(output_csv)  # 调取输出的数据文件

    return StockDf


def genFeature(StockDf, file_name, win_size=3):
    # Generating moving window features
    problem_file = open(file_name, 'w+')
    DfLen = len(StockDf.index)  # 长度
    for n in range(0, DfLen - win_size):
        predic_idx = n + win_size
        predict = 0
        predict = StockDf.ix[predic_idx, 'rise']  # 收益率预测
        predict = predict * 10  # 1= rise 10%
        Sample = str(predict) + ' '

        feature_id = 1
        feature_val = 0
        for j in range(n, n + win_size):
            Sample += getFeatureSample(StockDf, j, 'open', feature_id)  # 获得开盘价指标
            feature_id += 1
            Sample += getFeatureSample(StockDf, j, 'high', feature_id)  # 获得最高价指标
            feature_id += 1
            Sample += getFeatureSample(StockDf, j, 'close', feature_id)  # 获得收盘价指标
            feature_id += 1
            Sample += getFeatureSample(StockDf, j, 'low', feature_id)  # 获得最低价指标
            feature_id += 1
            Sample += getFeatureSample(StockDf, j, 'volume', feature_id)  # 获得成交量
            feature_id += 1
            Sample += getFeatureSample(StockDf, j, 'ema', feature_id)  # 获取计算出的EMA指标
            feature_id += 1

        Sample += '\n'
        problem_file.write(Sample)

    problem_file.close()
    print('\n sample number: ' + str(n + 1) + '\n feature number: ' + str(feature_id - 1))

    del problem_file
    del StockDf


if __name__ == '__main__':
    # print(sys.path)
    for i in range(1, len(sys.argv)):
        print ("Argument", i, sys.argv[i])

    StockCode = sys.argv[1]  # 获取股票代码
    Df = fetchStockData(StockCode, StockCode + '.csv')
    genFeature(Df, 3, StockCode)
