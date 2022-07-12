# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 18:40 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '三次元美图'
__plugin_usage__ = r"""
本接口用于随机显示一些图片,为网络接口(目前不太稳定)

发送 "三次元"即可使用~ https://cdn.seovx.com/ha/?mom=302
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('three_dimensional', aliases=("三次元", '三次元美图', "美图", "美女图"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    r1, r2, r3 = await three_dimensional()
    # 向用户发送结果
    await session.send(r1)
    await session.send(r2)
    await session.send(r3)


async def three_dimensional():
    try:
        # img_url = "https://api.pingping6.com/tools/acg3/"
        url = "http://api.weijieyue.cn/api/youhuo/api.php"
        r = requests.get(url)
        # print(r.url)
        img = "[CQ:image,file=" + str(r.url) + ",]"
        # link = {
        #     "type": "share",
        #     "data": {
        #         "url": "https://api.pingping6.com/tools/acg3/",
        #         "title": "三次元美图"
        #     }
        # }
        i = "https://cdn.seovx.com/ha/?mom=302"
        r2 = requests.get(i)
        ii = "[CQ:image,file=" + str(r2.url) + ",]"

        url3 = "http://api.weijieyue.cn/api/gqtp/api.php?msg=美女"
        r3 = requests.get(url3).text
        i3 = "[CQ:image,file=" + str(r3) + ",]"

        return img, ii, i3

    except Exception as e:
        return f"出错啦:{e}"
