# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 22:46 
# @IDE : PyCharm(2022.1.1) Python3.9.12


import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '身份证号解析(私聊)'
__plugin_usage__ = r"""
身份证号解析

发送"身份证号解析+身份证号"使用 返回生日,性别,星座,地址信息等...
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('id', aliases="身份证号解析", only_to_me=True)
async def handle_first_receive(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    id = session.current_arg_text.strip()
    if not id:
        id = (await session.aget(prompt='请发送您想查询的身份证号 !!请勿在群中使用该功能!!')).strip()
        # 如果用户只发送空白符，则继续询问
        while not id:
            id = (await session.aget(prompt='身份证号不能为空呢，请输入 !!请勿在群中使用该功能!!')).strip()
    result = await id_info(int(id))
    await session.send(result)


async def id_info(id: int):
    try:
        url = "https://v2.alapi.cn/api/idcard"
        payload = "token=请自己手动去获取密钥&id={}".format(id)
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        # pprint(response)
        x = response['data']
        res = "生日:" + x["birthday"] + "\n" \
              + "年龄:" + ("男" if x["sex"] == 1 else "女") + "\n" \
              + "性别:" + x["zodiac"] + "\n" \
              + "生肖:" + x["age"] + "\n" \
              + "星座:" + x["constellation"] + "\n" \
              + "地址信息:" + x['address'] + "\n"

        return res

    except Exception as e:
        return f"出错啦:{e}"
