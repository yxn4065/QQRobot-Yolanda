# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 20:12 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = 'QQ音乐'
__plugin_usage__ = r"""
随机一首QQ音乐,听你想听~(开发中)

发送"QQ音乐"随机返回一首QQ音乐热门歌曲~
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('NetEaseCloud_music_review', aliases=("QQ音乐", "qq音乐"))
async def handle_first_receive(session: CommandSession):
    # 获取数据并向用户发送结果
    res = "随机一首QQ音乐,听你想听~(开发中)\n音乐聚合:http://mp3.lmwljz.com/"
    await session.send(res)


async def NetEaseCloud_music():
    try:
        url = "https://v2.alapi.cn/api/comment"
        payload = "token=请自己手动去获取密钥&id="
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        # print("歌曲：", response["data"]['title'], response["data"]['description'])
        # print("热评: ", response["data"]['comment_content'])
        song_id = response["data"]["song_id"]

        # qq 163 xm 分别表示使用 QQ音乐、网易云音乐、虾米音乐
        res = [{
            "type": "music",
            "data": {
                "type": "qq",
                "id": str(song_id)
            }
        }]
        # res = f"[CQ:music, type=163, id={song_id}]"
        describe = "歌曲：" + response["data"]['title'] + "\n" + response["data"]['description'] \
                   + "\n歌曲id: " + str(song_id) + "\n(可发送 网易云热评+歌曲id 获取该歌曲热评)"

        return res, describe

    except Exception as e:
        # print(e)
        return f"出错啦:{e}"
