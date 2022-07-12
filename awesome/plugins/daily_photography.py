# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 14:02 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '今日摄影'
__plugin_usage__ = r"""
one 一个，每日一个摄影

发送 "今日摄影" 获取~
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('daily_photography', aliases="今日摄影")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    message, res = await daily_photography()
    # 向用户发送结果
    await session.send(message)
    await session.send(res)


async def daily_photography():
    try:
        url = "https://v2.alapi.cn/api/one/photo"
        payload = "token=请自己手动去获取密钥&date=2021-04-21"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        message = [
            {
                "type": "image",
                "data": {
                    "file": response['data']['cover'],
                }
            }, {
                "type": "text",
                "data": {
                    "text": response['data']['subtitle']
                }
            }
        ]
        res = response['data']['content']
        return message, res

    except Exception as e:
        return f"出错啦:{e}"
