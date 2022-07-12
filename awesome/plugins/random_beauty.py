# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 23:15 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '随机美图'
__plugin_usage__ = r"""
在线美图~提供两个不同的接口进行获取.

发送"随机美图"获取随机美图~
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('random_beauty', aliases=("随机美图", "养养眼"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    img_url1 = "https://cdn.seovx.com/?mom=302"
    r1 = requests.get(img_url1)
    result1 = "[CQ:image,file=" + str(r1.url) + ",]"
    # 向用户发送结果
    await session.send(result1)

    img_url2 = "https://api.7585.net.cn/img/api.php"
    r2 = requests.get(img_url2)
    result2 = "[CQ:image,file=" + str(r2.url) + ",]"
    await session.send(result2)
