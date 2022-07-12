# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/14 22:24 
# @IDE : PyCharm(2022.1) Python3.9.12
import csv
import random

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '王者美图'
__plugin_usage__ = r"""
王者荣耀cosplay美图鉴赏

直接发送 "王者美图",随机从图库中给你返回一张图~
发送 ""王者荣耀"",随机从图库中给你返回一张图~
"""

EXPR_DONT_UNDERSTAND = (
    '>>出现这句话请联系开发人员~!'
)


def get_pictures_urls() -> list:
    """在1-6327之间生成3位随机数,即随机读取3行作为图片url列表返回"""
    # x = random.randint(0, 6328)
    # print(x)
    # [0,6328)生成完全随机的5个数，这五个数被限制不能重复
    x = random.sample(range(0, 6328), 3)
    # print(x)

    with open('../../temp/url_all.csv', 'r') as f:
        img_url = csv.reader(f)
        all_url = list(img_url)
        # a = random.sample(all_url, 5) #在固定列表中随机取多个数
        r1 = all_url[x[0]][0]
        r2 = all_url[x[1]][0]
        r3 = all_url[x[2]][0]

    return [r1, r2, r3]


def get_pictures_url() -> str:
    """随机返回一张图片url"""
    # with open('../../temp/url_all.csv', 'r') as f:
    with open('/root/yxn/root/CQ-GO/QQRobot/awesome-bot/temp/url_all.csv', 'r') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        # print(chosen_row[0])

    return chosen_row[0]


@on_command('king_glory_cosplay_beauty_picture_appreciation',
            aliases=("王者美图", "图来", "cosplay美图", "随机一图"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 发送请求等待结果
    url = get_pictures_url()
    result = await get_img(url)
    # 向用户发送查询结果
    await session.send(message=result)


async def get_img(url: str):
    # header = {
    #     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    #                   "Chrome/100.0.4896.127 Safari/537.36"}
    # try:
    #     name = url[-10]
    #     res = requests.get(url=url, headers=header).content
    #     with open(name, 'wb') as f:
    #         f.write(res)
    #
    # except Exception as e:
    #     # print(e)
    #     return f"获取图片出现错误啦~：{e}"

    return "[CQ:image,file=" + url + ",]"


@on_command('King_of_Glory', aliases="王者荣耀")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    img_url = "https://api.r10086.com/img-api.php?type=王者荣耀"
    r = requests.get(img_url)
    result = "[CQ:image,file=" + str(r.url) + ",]"
    # 向用户发送结果
    await session.send(result)
