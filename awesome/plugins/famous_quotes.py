# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 22:00 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import random
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '名人名言'
__plugin_usage__ = r"""
随机返回一条古今中外名人名言

发送 "名人名言" 获取内容
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('famous_quotes', aliases="名人名言", only_to_me=True)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await famous_quotes()
    # 向用户发送结果
    await session.send(result)


async def famous_quotes():
    try:
        url = "https://v2.alapi.cn/api/mingyan"
        i = random.randint(1, 45)
        payload = "token=请自己手动去获取密钥&format=json&typeid={}".format(i)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        return response['data']['content'] + "---" + response['data']['author']

    except Exception as e:
        return f"出错啦:{e}"
