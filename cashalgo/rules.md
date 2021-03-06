# 2016年度大中华区校际演算交易竟赛

> 时富量化金融平台

> 规则及技术注释

## 交易产品(Trading Products)

> 参赛者的交易策略只限买卖以下香港交易所旗下的证券

* HHI: 恒生指数期货及期权
* HSI: 小型恒生指数期货及期权
* MHI: 恒生中国企业指数期货及期权
* MCH: 小型国企指数期货

大会将提供的市场数据包括恒生指数期货及期权, 恒生中国企业指数期货及期权, 小型恒生指数期货及期权和小型国企指数期货. 有关数据集包括每秒的最后交易记录及买卖价的最新资料. 有关数据来自 2016 年 1 月至 6 月期间, 每个交易日上午及下午时段的正常交易时间, 但不包括收市后期货交易时段的期货交易数据. 请注意, 有关时段的数据只可用作编写交易策略. 决赛阶段会以相同结构的数据集作评核, 但参赛者不会获告知有关数据来自哪个时段, 因此大会不建议参赛者过度拟合数据集.

## 交易成本(Transaction Cost)

> 每种产品的交易成本总括如下

* 恒生指数期货及期权: 每边每张合约港币 $15.00
* 恒生中国企业指数期货及期权: 每边每张合约港币 $8.00
* 小型恒生指数期货: 每边每张合约港币 $5.00
* 小型恒生指数期权: 每边每张合约港币 $3.00
* 小型国企指数期货: 每边每张合约港币 $3.00

## 初始资本(Initial Capital)

大会对于初始资本的规定是宽松的, 参赛团队可以在后台环境里自行设定交易策略的初始资本. 在决赛阶段, 每个团队都需要为自己的策略建议一个最小初始资本, 时富量化金融集团会把此数值设定为回溯测试的初始资本, 以得出最终结果.

比赛中假设损益与资本成线性关系, 例如初始资本加倍, 则绝对损益也会相应加倍, 回报率因此维持不变. 另外, 为简单起见, 比赛假设用家没有市场影响力.

## 按金要求(Margin Requirement)

大会将采用名为 SPAN 的客户按金计算方法. SPAN 由芝加哥商业交易所 (CME) 设计推出, 基于风险和考虑整个投资组合来计算每日按金要求. 它找出持仓的期货和期权投资组合的总体风险, 并计算覆盖此风险的按金要求.

若希望得知更多细节, 请浏览以下网页: <https://www.hkex.com.hk/eng/market/rm/rm_dcrm/rm_dcrm_clearing/futrsksys2.htm>

参赛者应注意他们的整体持仓量, 如果在回溯测试时发现按金未达要求, 团队有可能被取消资格. 因此, 参赛团队应小心设定初始资本的数量, 既能用来维持按金要求, 同时避免令回报率太低.

## 大额交易与低流动性产品的处理(Large Order and Illiquid Products Handling)

系统包括每秒的买卖价的最新资料, 每项资料均有价钱和数量. 定单应采用市场价格, 并把时效设定为「立刻执行或取消」(Immediate or Cancel). 例如当买卖价为 99$/101$, 买单将会以 101 元成交, 而卖单则会以 99 元成交. 模拟交易系统会利用数量来限制成交量.

假设一个算法打算在 2016 年 1 月 4 日开市时买入 3 张 HSIF 6 期指合约, 系统会寻找当时的买卖价资料. 在 2016 年 1 月 4 日 9 时 15 分, 一项卖价资料显示当时的沽售价是 21854, 而沽售量是 2. 因此, 算法只成功购入 2 张合约, 剩下的 1 张合约则被取消. 你可以利用函数 `ts[“account”].get_trades()` 来查看定单状况 (order status), 系统会显示订单只是部分完成(OrderStatus.PartiallyFilled).

同时, 请注意某些低流动性的产品可能长时期没有买卖价的更新, 如果你设定算法在某个特定时段内行动, 将有未能成功执行定单的风险.

所以, 我们建议在实行大额交易或低流动性产品交易时, 应检查当时的持仓数量. 你也可以用函数 `ts[“account”].get_trades()` 来查看是否有不正常的交易条目.

## 决赛阶段评核(Final Round Evaluation)

决赛阶段的参赛队伍需要编写他们提出的交易策略, 大会会以相同结构的数据集作回溯测试, 但参赛者不会获告知有关数据来自哪个时段. 大会将计算各项关键绩效指标 (如损益, 投资回报率, 夏普比率等), 决赛阶段的评核详情将在完成初赛后发送给各进入决赛的团队. 参赛者应紧记一个能平衡回报和风险的策略将会被优先选取.
