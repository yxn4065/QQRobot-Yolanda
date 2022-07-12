# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 22:20 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '歇后语'
__plugin_usage__ = r"""
随机返回一句歇后语

发送"歇后语"获取
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('after_a_break', aliases="歇后语")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await after_a_break()
    # 向用户发送结果
    await session.send(result)


async def after_a_break():
    try:
        url = "https://v2.alapi.cn/api/xhy/random"
        payload = "token=请自己手动去获取密钥"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        return response['data']['riddle'] + "--- " + response['data']['answer']


    except Exception as e:
        return f"出错啦:{e}"
