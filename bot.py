# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 13:21 
# @IDE : PyCharm(2022.1) Python3.9.12
# pip install -U quart

# import preprocessing
import nonebot
import config
from os import path

if __name__ == '__main__':
    nonebot.init(config)  # 使用默认配置初始化 NoneBot 包
    nonebot.load_builtin_plugins()  # 加载 NoneBot 内置的插件
    # 加载个人的插件
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'awesome', 'plugins'),
        'awesome.plugins'
    )

    # nonebot.run(host='127.0.0.1', port=8081)  # 在地址 127.0.0.1:8081 运行 NoneBot
    nonebot.run()
