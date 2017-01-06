#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import libsvm.python.easy_predict as predict  # 调用SVM预测函数
import libsvm.python.easy_train_svr_b1 as train  # 调用SVM函数训练集
import stockfeature.stock_feature_svr as feature  # from StockFeature import stock_feature_svr

if __name__ == '__main__':
    # print(sys.path)
    for i in range(1, len(sys.argv)):
        print("Argument", i, sys.argv[i])

    StockCode = sys.argv[1]
    Df = feature.fetchStockData(StockCode, StockCode + '.csv')  # 读取ｃｓｖ文件　提取特征
    feature.genFeature(Df, StockCode, 3)  # moving window size=3

    train.easy_train(StockCode)  # 使用训练数据进行训练

    predict(StockCode, StockCode)
    # 预测股价　返回值pred_label，它是一个列向量，第i个元素代表第i个测试样本的预测类别
