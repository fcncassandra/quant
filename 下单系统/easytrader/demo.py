## 1 安装包
# pip install easytrader -i https://pypi.tuna.tsinghua.edu.cn/simple
# https://github.com/shidenggui/easytrader


## 2 安装同花顺客户端
# 使用老版本同花顺，或者下载easytrader源码修改
# 链接：https://pan.baidu.com/s/14JYEktI4_cRXqRDbbAYrbA  提取码：826a

## 3 连接操作
import easytrader
# 设置交易客户端类型
# 通用型客户端，设置同花顺即可
user = easytrader.use('ths')

# 启动并连接客户端
user.connect(r'F:\finance\同花顺')

# 查看User信息
user.__dict__
'''
{'_config': easytrader.config.client.CommonConfig,
 '_app': <pywinauto.application.Application at 0x17b7e8ad630>,
 '_main': <pywinauto.application.WindowSpecification at 0x17b7c655668>,
 '_toolbar': <pywinauto.application.WindowSpecification at 0x17b009f1898>}
'''
user.broker_type
# 查资金
user.balance

# 查持仓
user.position

# 委托
user.buy('510300', 4.5, 100)
# 当日委托
user.today_entrusts
# 当日成交
user.today_trades
# 撤单，传入委托端的编号
# 周末的运行状态是未报，所以未报的状态是不能撤单的
user.cancel_entrust(13)

## 4 建议
# 稳健性：easytrader的BUG估计不少，建议实盘交易小资金量先试
# 实时性：由于其是基于GUI图形界面实现自动化交易接口，并非API层面，因此实时性不会很高，不适合秒级策略
# 合规性：类似于一个外挂性质的工具，在我国监管体系下并不合规