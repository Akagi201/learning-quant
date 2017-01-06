# stock-svm

使用了libsvm库中的函数 使用前需要安装对应版本的libsvm

主函数是test.py

用到的其他函数是位于StockFeature文件夹里的stock_feature 和 stock_feature_svr 的py文件

## Notes
* 数据调用使用了 tushare.
* `600111.csv` 是代码为 600111 的股票相应数据.
* `stock_feature` 注释中写了从 tushare 中获取数据的过程.
* 移植到其他平台的时候应该只需要将 tushare 换成平台的相应调取数据的库.
* Features: 前N天日K线 + EMA
* Prediction: 下一个交易日的涨跌幅 (1:10%; -1:-10%).

```
Prob. model for test data: target value = predicted value + z,
z: Laplace distribution e^(-|z|/sigma)/(2sigma),sigma=0.15668
Mean squared error = 0.0486415 (regression)
Squared correlation coefficient = 0.0191634 (regression)
```

## Run
* `python test.py 600111`

## Refs
* [Tushare](http://tushare.waditu.com/)
* [LibSVM]()http://www.csie.ntu.edu.tw/~cjlin/libsvm/)




