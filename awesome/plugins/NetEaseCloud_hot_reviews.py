# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 23:22 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '网易云热评'
__plugin_usage__ = r"""
时间久了，那种感动依然不可褪去。 你能在这倾听别人的故事，亦或许是你的故事

发送 "网易云热评 歌曲id"调用,歌曲id可通过发送"网易云歌曲"获取哦~
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明插件{__file__}有问题,建议进行排查!'


@on_command('NetEaseCloud_hot_reviews', aliases=("网易云热评", "网易云乐评", "网易云"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    id = session.current_arg_text.strip()
    if not id:
        music, res = neteasy()
        await session.send(music)
        await session.send(res)
    else:
        result = await hot_reviews(int(id))
        await session.send(result)


async def hot_reviews(id: int) -> str:
    try:
        url = "https://v2.alapi.cn/api/comment"
        payload = "token=请自己手动去获取密钥&id={}".format(id)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        res = "歌曲：" + response["data"]['title'] + "\n" + response["data"]['description'] + "\n\n"
        for n, i in enumerate(response["data"]['hot_comment']):
            # print(n, i['content'])
            res += str(n) + " " + i['content'] + "\n\n"
        res += "..."
        return res

    except Exception as e:
        return f"出错啦:{e}"


async def neteasy():
    import re
    url = "https://api.uomg.com/api/comments.163?format=json"
    r = requests.get(url).json()
    res = r['data']['name'] + " " + r['data']['artistsname'] + "\n"
    res += r['data']['content'] + "\n"
    print("url:", r['data']['url'])
    x = re.findall("id=(\d+)", r['data']['url'])
    # print(str(x[0]))
    music = [{
        "type": "music",
        "data": {
            "type": "163",
            "id": str(x[0])
        }
    }]

    return music, res
