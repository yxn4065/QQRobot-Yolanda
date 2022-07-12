# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 21:03 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import nonebot
import requests
from nonebot import CommandSession, IntentCommand, NLPSession, on_command, on_natural_language, scheduler

# 使用帮助
__plugin_name__ = '每日60s早报'
__plugin_usage__ = r"""
每日60s早报,60s带你看世界

发送 "早报"即可获取~
"""


@on_command('_60', aliases=("早报", "今日早报", "晨报"), only_to_me=False)
async def handle_first_receive(session: CommandSession):
    txt, img = await _60()
    # 向用户发送查询结果
    await session.send(img)
    await session.send(txt)


async def _60():  # 每日60s早报
    try:
        url = "https://v2.alapi.cn/api/zaobao"
        payload = "token=请自己手动去获取密钥&format=json"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, headers=headers, data=payload).json()
        # pprint(response.json())
        mes = response['data']['date'] + "\n"
        mes += 'head_image: ' + response['data']['head_image'] + "\n"
        mes += 'image: ' + response['data']['image'] + "\n" + '早报内容: \n'
        for i in response['data']['news']:
            # print(i)
            mes += i
        mes += "\n" + response['data']['weiyu']

        img_url = response['data']['image']
        message1 = [
            {
                "type": "text",
                "data": {
                    "text": response['data']['weiyu']
                }
            }]
        message2 = [
            {
                "type": "image",
                "data": {
                    "file": img_url,
                }
            }
        ]
        return message1, message2

    except Exception as e:
        return f"出错啦:{e}"


# 不需要@直接进行响应
@on_natural_language(keywords={'早报'}, only_to_me=False)
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(80.0, '_60')

# # 设置定时发送
# @scheduler.scheduled_job('_60', day_of_week='0-6', hour=8, minute=00)
# async def demo():
#     bot = nonebot.get_bot()
#     group_id = int(bot.config.group_Test)
#     url = "https://v2.alapi.cn/api/zaobao"
#     payload = "token=请自己手动去获取密钥&format=json"
#     headers = {'Content-Type': "application/x-www-form-urlencoded"}
#     response = requests.request("POST", url, headers=headers, data=payload).json()
#     mes = response['data']['date'] + "\n"
#     mes += 'head_image: ' + response['data']['head_image'] + "\n"
#     mes += 'image: ' + response['data']['image'] + "\n" + '早报内容: \n'
#     for i in response['data']['news']:
#         print(i)
#         mes += i
#     mes += "\n" + response['data']['weiyu']
#     message = [
#         {
#             "type": "text",
#             "data": {
#                 "text": mes
#             }
#         },
#         {
#             "type": "image",
#             "data": {
#                 "file": response['data']['head_image'],
#             }
#         }
#     ]
#     await bot.send_group_msg(group_id=group_id, message=message)
