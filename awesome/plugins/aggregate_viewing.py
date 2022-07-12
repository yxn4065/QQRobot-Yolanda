# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 19:54 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '电影推荐'
__plugin_usage__ = r"""
里面数据很多,仍然懒得清洗,自己访问官网~

简猿影视官网 http://v.vopipi.cn/
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('aggregate_vivewing', aliases="影视聚合")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = "里面数据很多,懒得清洗,自己访问官网~\n简猿影视官网 http://v.vopipi.cn/\n无法打开请移步浏览器~"
    # 向用户发送结果
    await session.send(result)
