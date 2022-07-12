# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 22:02 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '随机诗词'
__plugin_usage__ = r"""
随机返回一篇古代诗词,一起来鉴赏吧~

发送"随机诗词"获取内容
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('poetry', aliases=("随机诗词", "古诗"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await poetry()
    # 向用户发送结果
    await session.send(result)


async def poetry():
    try:
        url = "https://v2.alapi.cn/api/shici"
        payload = "token=请自己手动去获取密钥&format=json&type=all"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        res = response['data']['content'] + "  ---" + response['data']['author'] + "\n"
        res += "诗词题:" + response['data']['origin'] + "\n" + "类别:" + response['data']['category']
        return res

    except Exception as e:
        return f"出错啦:{e}"
