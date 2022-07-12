# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 21:28 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import random

import requests
from datetime import datetime
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '历史上的今天'
__plugin_usage__ = r"""
获取当天历史上的几天数据

发送"历史上的今天"进行使用,默认查询当天~
如需要指定日期请发送"历史上的今天+日期" 
如 "历史上的今天 0520"
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'

today_date = datetime.now().strftime('%m%d')  # 获取当天日期时间,如0229


@on_command('today_in_history', aliases="历史上的今天", only_to_me=False)
async def handle_first_receive(session: CommandSession):
    date = session.current_arg_text.strip()
    if not date:  # 默认发送当天内容
        result = await today_in_history()
        await session.send(result)
    else:  # 如果用户制定了日期则返回对应日期内容
        global today_date
        today_date = datetime.now().strftime('%m%d')  # 获取当天日期时间,如0229
        result = await today_in_history(date)
        await session.send(result)


async def today_in_history(today=today_date):  # 历史上的今天
    global today_date
    today_date = datetime.now().strftime('%m%d')  # 获取当天日期时间,如0229
    try:
        url = "https://v2.alapi.cn/api/eventHistory"
        page = random.randint(1, 4)
        payload = "token=请自己手动去获取密钥&monthday={}&page={}".format(today, page)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        res = ""
        for i in response["data"]:
            res += i["date"] + i['title'] + "\n"
        return res

    except Exception as e:
        return f"出错啦:{e}"
