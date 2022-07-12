# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 23:42 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '开心一刻'
__plugin_usage__ = r"""
获取每日笑话，逗你开心,我是认真的哦~

发送"开心一刻"听我讲笑话吧~(数据来自互联网)
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('happy_moment', aliases="开心一刻")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await happy_moment()
    # 向用户发送结果
    await session.send(result)


async def happy_moment():
    try:
        url = "https://v2.alapi.cn/api/joke/random"
        payload = "token=请自己手动去获取密钥"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        # pprint(response)
        t = response['data']['title']
        res = "《%s》" % (t if t else "") + "\n"
        res += response['data']['content']

        return res

    except Exception as e:
        return f"出错啦:{e}"
