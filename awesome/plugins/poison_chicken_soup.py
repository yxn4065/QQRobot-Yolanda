# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 22:06 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '心灵鸡汤'
__plugin_usage__ = r"""
心灵毒鸡汤,治愈你的伤

快发送 "鸡汤" 获取一份美味的鸡汤吧~
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('poison_chicken_soup', aliases=("心灵鸡汤", "鸡汤", "毒鸡汤", "来一碗"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await poison_chicken_soup()
    # 向用户发送结果
    await session.send(result)


async def poison_chicken_soup() -> str:
    try:
        url = "https://v2.alapi.cn/api/soul"
        payload = "token=请自己手动去获取密钥&format=json"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        return response['data']['content']

    except Exception as e:
        return f"出错啦:{e}"
