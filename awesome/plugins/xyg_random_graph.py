# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 23:39 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = 'xyg随机图'
__plugin_usage__ = r"""
来源 xyg随机图 https://api.likepoems.com/

发送"xyg随机图"获取,过于随机,建议私聊发送~
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('cannot_be_sour', aliases=("xyg随机图", "xyg"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    img_url1 = "https://api.likepoems.com/pc"
    r1 = requests.get(img_url1)
    result1 = "[CQ:image,file=" + str(r1.url) + ",]"
    # 向用户发送结果
    await session.send(result1)

    img_url2 = "https://api.likepoems.com/pe"
    r2 = requests.get(img_url2)
    result2 = "[CQ:image,file=" + str(r2.url) + ",]"
    await session.send(result2)
