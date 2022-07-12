# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 0:09 
# @IDE : PyCharm(2022.1.1) Python3.9.12
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '名词解释'
__plugin_usage__ = r"""
直接发送名词即可,但目前识别成功率较低,正在强化学习当中~

https://www.termonline.cn/index  # 可直接访问术语在线官网
"""


@on_command('glossary', aliases="名词解释")
async def handle_first_receive(session: CommandSession):
    res = "[CQ:share,url=https://www.termonline.cn/index,title=【权威】术语在线]"
    await session.send(res)
    await session.send("直接给小Yo发送名词即可~，权威的请自己查询哦~")

