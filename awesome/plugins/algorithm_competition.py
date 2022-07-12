# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 17:38 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '算法竞赛'
__plugin_usage__ = r"""
了解最新算法竞赛~敢站你就来

发送 "算法竞赛"获取~
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('lgorithm_competition', aliases="算法竞赛")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await lgorithm_competition()
    # 向用户发送结果
    await session.send(result)


async def lgorithm_competition():
    try:
        url = "http://algcontest.rainng.com/"
        r = requests.get(url).json()
        # pprint(r)
        res = ""
        for each in r:
            res += 'oj: ' + each['oj'] + "\n"
            res += 'name: ' + each['name'] + "\n"
            res += 'startTime: ' + each['startTime'] + "\n"
            res += 'endTime: ' + each['endTime'] + "\n"
            res += 'link: ' + "\n" + each['link'] + "\n\n"
        res += "不要犹豫!你是最棒的~"
        return res

    except Exception as e:
        return f"出错啦:{e}"
