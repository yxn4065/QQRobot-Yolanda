# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 13:57 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '每日一文'
__plugin_usage__ = r"""
one 一个，每日一篇文章(维护中)

发送 "每日一文"获取今日文章~
"""


@on_command('article_of_the_day', aliases="每日一文")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await article_of_the_day()
    # 向用户发送结果
    await session.send(result)


async def article_of_the_day():
    try:
        url = "https://v2.alapi.cn/api/one"
        payload = "token=请自己手动去获取密钥&date=2021-04-21"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        # pprint(response)
        res = "《%s》 " % (response['data']['title']) + response['data']['subtitle'] + "\n"
        content = response["data"]["content"]

        res += (content.replace("</p><p>", "\n").replace("\u3000\u3000", "\t")
                .replace("<p>", "").replace("</p>", "").replace("<br>", ""))

        if len(res) >= 3000:
            res = res[0:3000]

        return res + "...\n(未结束可能字数超过最大允许内容)"

    except Exception as e:
        return f"出错啦:{e}"
