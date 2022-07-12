# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/14 23:33 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import json
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '必应壁纸'
__plugin_usage__ = r"""
必应壁纸(每日更新)

直接发送 "必应壁纸"获取~
发送"高清壁纸"随机获取一张壁纸图~
"""
EXPR_DONT_UNDERSTAND = '>>出现这句话请联系开发人员~!'


@on_command('bing_wallpaper', aliases="必应壁纸")
async def handle_first_receive(session: CommandSession):
    result, img = await bing_meitu()
    # 向用户发送查询结果
    await session.send(result)
    await session.send(img)


@on_command('HD_wallpaper', aliases="高清壁纸")
async def handle_first_receive(session: CommandSession):
    img_url = "https://api.ixiaowai.cn/gqapi/gqapi.php"
    r = requests.get(img_url)

    img = "[CQ:image,file=" + r.url + ",]"
    # 向用户发送查询结果
    await session.send(img)


async def bing_meitu():  # 必应美图
    url = "https://v2.alapi.cn/api/bing"
    payload = "token=请自己手动去获取密钥&format=json"
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, data=payload, headers=headers).json()
    # pprint(response.json())
    res = "每日一图 - 必应 -" + response['data']['enddate'] + "\n" + response['data']['copyright'] \
          + "\n" + response['data']['bing']
    img_url = response['data']['bing']
    img = "[CQ:image,file=" + img_url + ",]"
    # print("每日一图 - 必应 -", response['data']['enddate'])
    # print(response['data']['copyright'])
    # print(response['data']['bing'])
    return res, img
