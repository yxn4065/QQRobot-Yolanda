# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 21:53 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import random

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = 'Hitokoto一言'
__plugin_usage__ = r"""
Hitokoto

发送 "Hitokoto" 获取~
API_1: https://pa-1251215871.cos-website.ap-chengdu.myqcloud.com/
API_2: https://api.likepoems.com/yiyan/
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('Hitokoto_1', aliases=("Hitokoto", "Hitokoto一言", "ht一言"))
async def handle_first_receive(session: CommandSession):
    result = await Hitokoto_1()
    # 向用户发送查询结果
    await session.send(result)


@on_command('Hitokoto_2', aliases=("hitokoto", "一言", "来一句"))
async def handle_first_receive(session: CommandSession):
    result = requests.get("https://api.likepoems.com/yiyan/").text
    # 向用户发送查询结果
    await session.send(result)


async def Hitokoto_1():
    try:
        url2 = "https://api.likepoems.com/yiyan/"
        url = "https://v2.alapi.cn/api/hitokoto"
        type = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'a'])
        payload = "token=请自己手动去获取密钥&type={}&format=json".format(type)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        return response['data']['hitokoto'] + "  -----" + response['data']['from']

    except Exception as e:
        return f"出错啦:{e}"
