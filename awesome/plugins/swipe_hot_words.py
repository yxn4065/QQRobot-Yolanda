# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 23:36 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '刷屏热词'
__plugin_usage__ = r"""
获取网络上网络流行语或者梗

发送"刷屏热词"获取~，点击链接可看详细示意
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('swipe_hot_words', aliases='刷屏热词', only_to_me=False)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await swipe_hot_words()
    # 向用户发送结果
    await session.send(result + "\nend")


async def swipe_hot_words():
    try:
        url = "https://v2.alapi.cn/api/tophub/wiki"
        payload = "token=请自己手动去获取密钥"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        n = 0
        res = "热词:\n"
        for i in response['data']['hot']:
            res += i['title'] + "\n" + i['link'] + "\n"
            n += 1
            if n >= 10:
                break
        # res += "新词:\n"
        # for i in response['data']['new']:
        #     res += i['title'] + i['link'] + "\n"
        res += "最后更新: " + response['data']['last_update'] + "\n点击链接可查看详情~"
        # print("------>>", len(res))
        return res

    except Exception as e:
        return f"出错啦:{e}"
