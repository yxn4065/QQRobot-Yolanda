# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 22:33 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import re

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '随机美文'
__plugin_usage__ = r"""
获取一篇随机美文,陶冶你的情操~

原网站 https://meiriyiwen.com/
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('random_essay', aliases="随机美文")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await random_essay()
    # 向用户发送结果
    await session.send(result)


async def random_essay():
    try:
        url = "https://v2.alapi.cn/api/mryw/random"
        payload = "token=请自己手动去获取密钥"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        # pprint(response)
        s = (response['data']['title'])
        res = f"《{s}》 " + response['data']['author'] + "\n"
        content = response["data"]["content"]
        # 正则表达式匹配中文
        xx = u"([\u4e00-\u9fa5]+)"
        pattern = re.compile(xx)
        results = pattern.findall(content)
        res += " ".join(results)
        return res

    except Exception as e:
        return f"出错啦:{e}"
