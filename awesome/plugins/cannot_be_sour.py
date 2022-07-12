# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 23:32 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import asyncio
import time

import requests
from nonebot import CommandSession, get_bot, on_command

# 使用帮助
__plugin_name__ = '不可以涩涩'
__plugin_usage__ = r"""
不做介绍,自己看~内容可能略过于敏感(建议私聊使用!!!!)

内置指令"pixiv" "涩涩" "写真" "萝莉图" "画师图" "CG图"...等自己慢慢发掘~
群聊设置有自动撤回-内容质量不可控!
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'

bot = get_bot()


def time_choice(li: list, n: int) -> str:
    """
    用于获取随机值,弃用randam.choice()
    :param li: 列表
    :param n: 列表长度
    :return: url参数
    """
    x = int(time.time()) % n
    y = li[x]
    return str(y)


@on_command('cannot_be_sour', aliases=("涩涩", "写真", "萝莉图", "色图", "色色", "极品美女"))
async def handle_first_receive(session: CommandSession):
    li = ["少女写真1", "少女写真2", "少女写真3", "少女写真4", "少女写真5", "少女写真6",
          "死库水萝莉", "萝莉", "极品美女图片", "日本COS中国COS"]
    # t = int(time.time()) % 10
    y = time_choice(li, len(li))
    x = y.replace("'", "")
    # x = random.choice(li)
    img_url = "https://api.r10086.com/img-api.php?type={}".format(x)
    # content = "[CQ:image,file=" + img_url + ",type=flash]"
    r = requests.get(img_url)
    content = "[CQ:image,file=" + str(r.url) + ",]"
    ms1 = await session.send(content)
    # print(ms1)
    await session.send("该板块涉及内容未知,5s后自动撤回~")
    # await session.send("记得save~")
    # ms1 = await bot.send_msg(message=content)
    messageID = ms1['message_id']
    await asyncio.sleep(5)
    await bot.delete_msg(message_id=messageID)


@on_command('cannot_be_sour_pixiv', aliases=("画师图", "pixiv"))
async def handle_first_receive(session: CommandSession):
    li = ["P站系列1", "P站系列2", "P站系列3", "P站系列4"]
    y = time_choice(li, len(li))
    x = y.replace("'", "")
    # x = random.choice(li)
    img_url1 = "https://api.r10086.com/img-api.php?type={}".format(x)
    r1 = requests.get(img_url1)
    content = "[CQ:image,file=" + str(r1.url) + ",]"

    img_url2 = "https://api.likepoems.com/pixiv"
    r2 = requests.get(img_url2)
    content2 = "[CQ:image,file=" + str(r2.url) + ",]"
    await session.send(content2)

    ms1 = await session.send(content)
    # print(ms1)
    await session.send("风险板块内容未知~5s后自动撤回~")
    # ms1 = await bot.send_msg(message=content)
    messageID = ms1['message_id']
    await asyncio.sleep(5)
    await bot.delete_msg(message_id=messageID)


@on_command('cannot_be_sour_cg', aliases=("CG图", "CG系列"))
async def handle_first_receive(session: CommandSession):
    li = ["CG系列1", "CG系列2", "CG系列3", "CG系列4", "CG系列5"]
    # x = random.choice(li)
    y = time_choice(li, len(li))
    x = y.replace("'", "")

    img_url = "https://api.r10086.com/img-api.php?type={}".format(x)
    r = requests.get(img_url)
    content = "[CQ:image,file=" + str(r.url) + ",]"

    ms1 = await session.send(content)
    # print(ms1)
    await session.send("风险板块内容未知~5s后自动撤回~")
    # ms1 = await bot.send_msg(message=content)
    messageID = ms1['message_id']
    await asyncio.sleep(5)
    await bot.delete_msg(message_id=messageID)


@on_command('cannot_be_sour', aliases=("不可以色色系列", "不可以涩涩", "不可以色色"))
async def handle_first_receive(session: CommandSession):
    await session.send("主人说,小yo还是孩子,不可以涩涩~")
    await session.send('该模块内容来源未知~发送"使用帮助 不可以涩涩"获取口令吧~')
