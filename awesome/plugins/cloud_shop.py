# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 19:58 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '云小店'
__plugin_usage__ = r"""
欢迎使用云小店自助下单程序~全网低价

访问:yxn.yaoduxz.com
备用:yxn.qianhe123.com
[CQ:share,url=yxn.yaoduxz.com,title=云小店]
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('cloud_shop', aliases=("云小店", "刷网课"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = "欢迎使用云小店自助下单程序\n访问: yxn.yaoduxz.com\n备用: yxn.qianhe123.com"
    link = "[CQ:share,url=yxn.yaoduxz.com,title=云小店]"
    # 向用户发送结果
    await session.send(result)
