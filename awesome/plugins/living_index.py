# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 18:58 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from urllib.parse import quote, unquote

from jieba import posseg
from nonebot import CommandSession, NLPSession, on_command

# 使用帮助
__plugin_name__ = '生活指数'
__plugin_usage__ = r"""
查询当天的生活指数

输入"生活指数 城市"即可进行查询
"""


@on_command('living_index', aliases="生活指数", only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    city = session.current_arg_text.strip()
    if not city:
        city = (await session.aget(prompt='请输入你想查询的城市:')).strip()
        # 如果用户只发送空白符，则继续询问
        while not city:
            city = (await session.aget(prompt='要查询的城市不能为空呢，请重新输入')).strip()
    if not is_city(city):
        city = (await session.aget(prompt='您输入的不是一个城市名字哦,请重新输入:')).strip()
    # 获取查询结果
    result = await get_life(city)
    # 向用户发送查询结果
    await session.send(result)


async def get_life(city: str):  # 生活指数查询
    try:
        url = "https://v2.alapi.cn/api/weather/life"
        c = quote(city, 'utf-8')
        payload = "token=请自己手动去获取密钥&location={}".format(c)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        res = "当前城市: " + response['data']['basic']['admin_area'] + "\n"
        for i in response['data']['lifestyle']:
            if i['type'] == 'comf':
                res += "【体感】 " + i['brf'] + "\n" + i['txt'] + "\n"
            elif i['type'] == 'drsg':
                res += "【着装】 " + i['brf'] + "\n" + i['txt'] + "\n"
            elif i['type'] == 'flu':
                res += "【感冒】 " + i['brf'] + "\n" + i['txt'] + "\n"
            elif i['type'] == 'sport':
                res += "【运动】 " + i['brf'] + "\n" + i['txt'] + "\n"
            elif i['type'] == 'trav':
                res += "【旅行】 " + i['brf'] + "\n" + i['txt'] + "\n"
            elif i['type'] == 'uv':
                res += "【紫外线】 " + i['brf'] + "\n" + i['txt'] + "\n"
            elif i['type'] == 'air':
                res += "【空气质量】 " + i['brf'] + "\n" + i['txt'] + "\n"
            else:
                res += "【*】 " + i['brf'] + "\n" + i['txt'] + "\n"
        res += "最后更新时间: " + response['data']['update']['loc'] + "\n"
        return res

    except Exception as e:
        return f"查询出错啦:{e}"


async def is_city(city):
    """判断是否为城市名"""
    # 对消息进行分词和词性标注
    word = posseg.lcut(city)
    if word.flag == 'ns':
        return True
    else:
        return False
