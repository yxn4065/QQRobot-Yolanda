# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 21:45 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '舔狗日记'
__plugin_usage__ = r"""
卑微的爱情舔狗

发送"舔狗日记" 获取内容~
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('dog', aliases="舔狗日记", only_to_me=False)
async def handle_first_receive(session: CommandSession):
    result = await dog_licking_diary()
    # 向用户发送查询结果
    await session.send(result)


async def dog_licking_diary():
    """卑微的爱情舔狗"""
    try:
        url = "https://v2.alapi.cn/api/dog"
        payload = "token=请自己手动去获取密钥&format=json"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        return response["data"]["content"]

    except Exception as e:
        return f"出错啦:{e}"
