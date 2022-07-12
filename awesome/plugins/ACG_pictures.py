# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 21:18 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = 'ACG图片'
__plugin_usage__ = r"""
发送"ACG"或者"随机一图"获取

本接口服务由RABBITAPI(https://kafuuchino.com.cn)提供
"""

EXPR_DONT_UNDERSTAND = (
    '>>出现这句话说明该插件有问题,建议进行排查!'
)


@on_command('ACG_pictures', aliases=("ACG", "ACG图片", "随机图片"))
async def handle_first_receive(session: CommandSession):
    result = await acg_pic()
    # 向用户发送查询结果
    await session.send(result)


async def acg_pic():
    try:
        url = "https://rabbit-api.com/"  # ACG图片API
        headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 9.0; Pixel 2 Build/OPD3.170816.012)"}
        response = requests.get(url).json()
        img_url = str(response['data']['url'])
        return "[CQ:image,file=" + img_url + "]"

    except Exception as e:
        return f"获取图片失败:{e}"
