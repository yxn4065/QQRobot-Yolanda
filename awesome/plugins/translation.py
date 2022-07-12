# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/17 22:03 
# @IDE : PyCharm(2022.1.1) Python3.9.12

# 使用帮助
__plugin_name__ = '翻译'
__plugin_usage__ = r"""
翻译功能,支持中英互译

发送 "翻译 待翻译内容" 获取结果~
(翻译来源青云客API)
"""

import requests
from nonebot import CommandSession, on_command


@on_command('translation', aliases=("翻译", "中英互译"))
async def weather(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    word = session.current_arg_text.strip()
    if not word:
        await session.send('请发送 "翻译 待翻译内容" 执行该操作吧~')
    result = await translation(word)

    await session.send(result)


async def translation(word):
    try:
        url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=翻译 {}".format(word)
        r = requests.get(url).json()
        # print(r['content'].replace('{br}', '\n'))
        res = str(r['content'].replace('{br}', '\n'))
        return res

    except Exception as e:
        return f"出错啦:{e}"
