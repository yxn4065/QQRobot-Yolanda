# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 21:50 
# @IDE : PyCharm(2022.1.1) Python3.9.12

from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '今日热榜'
__plugin_usage__ = r"""
数据清洗太麻烦了,自己访问官网吧~(开发中)

https://tophub.today/
https://api.vvhan.com/api/hotlist
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command("todays_hot_list", aliases='今日热榜', only_to_me=False)
async def handle_first_receive(session: CommandSession):
    result = "懒得爬,数据清洗太麻烦了,自己访问官网吧~(无法打开请移步浏览器)\nhttps://tophub.today/\n" \
             "API 接口: https://api.vvhan.com/api/hotlist"
    await session.send(result)
    link = [{
        "type": "share",
        "data": {
            "url": "https://tophub.today/",
            "title": "今日热榜总榜"
        }
    }]
    await session.send(link)
