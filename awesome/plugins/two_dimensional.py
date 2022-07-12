# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 18:44 
# @IDE : PyCharm(2022.1.1) Python3.9.12


import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '二次元美图'
__plugin_usage__ = r"""
本接口用于随机显示一张二次元图片,只提供图片！

发送 "二次元"即可使用~ (刺激)
发送 "mc酱"获取一张MC酱动漫图~
本站接口由小歪API提供（https://api.ixiaowai.cn/）
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('two_dimensional', aliases="二次元", only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result, r2 = await two_dimensional()
    # 向用户发送结果
    await session.send(result)
    await session.send(r2)


async def two_dimensional():
    try:
        # img_url = "https://api.pingping6.com/tools/acg2/"
        img_url = "https://api.mtyqx.cn/api/random.php"
        r1 = requests.get(img_url)
        img = "[CQ:image,file=" + str(r1.url) + ",]"

        img_url2 = "https://cdn.seovx.com/d/?mom=302"
        r2 = requests.get(img_url2)
        img2 = "[CQ:image,file=" + str(r2.url) + ",]"
        return img, img2

    except Exception as e:
        return f"出错啦:{e}"


@on_command('two_dimensional_mc', aliases="mc酱", only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await two_dimensional_mc()
    # 向用户发送结果
    await session.send(result)


async def two_dimensional_mc():
    try:
        img_url = "https://api.ixiaowai.cn/mcapi/mcapi.php"
        r = requests.get(img_url)
        img = "[CQ:image,file=" + str(r.url) + ",]"
        return img

    except Exception as e:
        return f"出错啦:{e}"
