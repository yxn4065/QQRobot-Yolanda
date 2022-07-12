# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/20 22:15 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '颜值视频'
__plugin_usage__ = r"""
随机返回一个plmm,调用三方接口~

发送 "颜值视频"即可使用~ 默认是plmm.
看小哥哥请发送 "plgg"~
发送 "抖音网红" 获取抖音网红视频~
http://api.weijieyue.cn/api/kuaishou/yanzhi.php
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('kuaishou_beauty_video', aliases=("快手视频", '颜值视频', "随机视频", "快手美女", "plmm"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    r1, r2 = await kuaishou_mn()
    # 向用户发送结果
    await session.send(r1)
    await session.send(r2)


async def kuaishou_mn():
    try:
        url = "http://api.weijieyue.cn/api/kuaishou/yanzhi.php?xl=美女&type=js"
        r = requests.get(url).json()
        mp4 = {
            "type": "video",
            "data": {
                "file": r['视频链接']
            }
        }
        res = "用户: " + r['用户'] + "\n标题: " + r['标题'] + '\n播放量: ' + str(r['播放量']) \
              + "\n收藏数: " + str(r["收藏数"]) + "\n发布时间: " + r['发布时间'] + "\n"
        return mp4, res

    except Exception as e:
        return f"出错啦:{e}"


@on_command('plgg', aliases=("plgg", "快手帅哥"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    r1, r2 = await kuaishou_sg()
    # 向用户发送结果
    await session.send(r1)
    await session.send(r2)


async def kuaishou_sg():
    try:
        url = "http://api.weijieyue.cn/api/kuaishou/yanzhi.php?xl=帅哥&type=js"
        r = requests.get(url).json()
        mp4 = {
            "type": "video",
            "data": {
                "file": r['视频链接']
            }
        }
        res = "用户: " + r['用户'] + "\n标题: " + r['标题'] + '\n播放量: ' + str(r['播放量']) \
              + "\n收藏数: " + str(r["收藏数"]) + "\n发布时间: " + r['发布时间'] + "\n"
        return mp4, res

    except Exception as e:
        return f"出错啦:{e}"


@on_command('kuaishou_funny', aliases=("搞笑视频", "开心视频", "来个搞笑视频"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    r1, r2 = await kuaishou_funny()
    # 向用户发送结果
    await session.send(r1)
    await session.send(r2)


async def kuaishou_funny():
    try:
        url = "http://api.weijieyue.cn/api/kuaishou/gaoxiao.php?type=js"
        r = requests.get(url).json()
        mp4 = {
            "type": "video",
            "data": {
                "file": r['视频链接']
            }
        }
        res = "用户: " + r['用户'] + "\n标题: " + r['标题'] + '\n播放量: ' + str(r['播放量']) \
              + "\n收藏数: " + str(r["收藏数"]) + "\n发布时间: " + r['发布时间'] + "\n"
        return mp4, res

    except Exception as e:
        return f"出错啦:{e}"


@on_command('douying_funny', aliases='抖音网红', only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    r1, r2 = await kuaishou_funny()
    # 向用户发送结果
    await session.send(r1)
    await session.send(r2)


async def douyin_funny():
    try:
        url = "http://api.weijieyue.cn/api/douyin/api.php?n=网红"
        r = requests.get(url).text
        v = r.split("播放链接：")[-1]
        r = requests.get(url).json()
        mp4 = {
            "type": "video",
            "data": {
                "file": v
            }
        }

        return mp4

    except Exception as e:
        return f"出错啦:{e}"
