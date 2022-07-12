# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 19:08
# @IDE : PyCharm(2022.1) Python3.9.12
import json
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '查快递'
__plugin_usage__ = r"""
快递查询

查快递 [快递单号]
"""
EXPR_DONT_UNDERSTAND = (
    '>>出现这句话请联系开发人员~!'
)


@on_command('express_inquiry', aliases="查快递")
async def handle_first_receive(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    number = session.current_arg_text.strip()
    if not number:
        number = (await session.aget(prompt='请输入你想查询的快递单号')).strip()
        # 如果用户只发送空白符，则继续询问
        while not number:
            number = (await session.aget(prompt='要查询的快递单号不能为空呢，请重新输入')).strip()
    # 获取查询结果
    result = await get_express(number)
    # 向用户发送查询结果
    await session.send(result)


async def get_express(number):
    try:
        token = "请自己手动去获取密钥"
        url = "https://v2.alapi.cn/api/kd?number={}&token={}".format(number, token)
        response = requests.get(url).json()
        res = "查询到快递信息如下:" + "\n" + "快递单号: " + response['data']['nu'] + "\n" + "快递公司: " \
              + response['data']['com'] + "\n" + "物流信息: " + "\n"
        li = []
        for i in response['data']['info']:
            # print(i['content'], i['time'])
            li.append(i['content'])
            res += str(li).replace("[", "").replace("]", "").replace("\'", "") + "\n"
            li.clear()
            li.append(i['time'])
            res += "time:" + str(li).replace("[", "").replace("]", "").replace("\'", "") + "\n\n"
            li.clear()
        res += "查询结束,以上内容来自alapi接口。(该消息在60s后自动撤回)"
        return res

    except Exception as e:
        # print(e)
        return f"查询快递单号出错误啦~：{e}"
