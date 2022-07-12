# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 21:02 
# @IDE : PyCharm(2022.1) Python3.9.12

# 要获取 bot 对象，可以通过如下两种方式：
# import nonebot
# from nonebot import session

# bot = session.bot
# bot = nonebot.get_bot()
# await bot.send_private_msg(user_id=1912047718, message='你好～')

"""主动发送消息和调用 API 的例子"""
# await bot.send_private_msg(user_id=12345678, message='你好～')
# await bot.send_group_msg(group_id=123456, message='大家好～')
#
# params = session.event.copy()
# del params['message']
# await bot.send_msg(**params, message='喵～')
#
# await bot.delete_msg(**session.event)
# await bot.set_group_card(**session.event, card='新人请改群名片')
# self_info = await bot.get_login_info()
# group_member_info = await bot.get_group_member_info(group_id=123456, user_id=12345678, no_cache=True)
from nonebot import CommandSession

"""https://github.com/botuniverse/onebot-11/blob/master/api/public.md"""
"""https://docs.go-cqhttp.org/api/#%E5%8F%91%E9%80%81%E7%A7%81%E8%81%8A%E6%B6%88%E6%81%AF"""

# import requests
# data = "天气 重庆"
# response = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(data))
# print(response.status_code)
# # print(response.text)
# res = response.json()
# print(res["content"])

# import urllib
# import gzip
# import json
#
# def get_weather(city: str):
#     cityname = city
#     url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(
#         cityname)  # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
#     weather_data = urllib.request.urlopen(url).read()  # 发出请求并读取到weather_data
#     weather_data = gzip.decompress(weather_data).decode('utf-8')  # 以utf-8的编码方式解压数据
#     weather_dict = json.loads(weather_data)  # 将json数据转化为dict数据
#     print(weather_dict)
#     if weather_dict.get('desc') == 'invilad-citykey':
#         print("木有这个天气...")
#         return f"木有这个天气..."
#     elif weather_dict.get('desc') == 'OK':
#         forecast = weather_dict.get('data').get('forecast')
#         startoday = '城市：' + weather_dict.get('data').get('city') + '\n' \
#                     + '日期：' + forecast[0].get('date') + '\n' \
#                     + '温度：' + weather_dict.get('data').get('wendu') + '℃\n' \
#                     + '高温：' + forecast[0].get('high') + '\n' \
#                     + '低温: ' + forecast[0].get('low') + '\n' \
#                     + '风向：' + forecast[0].get('fengxiang') + '\n' \
#                     + '风力：' + forecast[0].get('fengli') + '\n' \
#                     + '天气：' + forecast[0].get('type') + '\n' \
#                     + '感冒：' + weather_dict.get('data').get('ganmao') + '\n'
#         print(startoday)
#         return startoday
#
#
# get_weather("重庆")


# import json
# from aiocqhttp.message import escape
# from nonebot import CommandSession
# from nonebot.helpers import render_expression
# from tencentcloud.common import credential
# from tencentcloud.common.profile.client_profile import ClientProfile
# from tencentcloud.common.profile.http_profile import HttpProfile
# from tencentcloud.tbp.v20190627 import models, tbp_client
# from typing import Optional
#
# # 定义无法获取腾讯智能机器人回复时的「表达（Expression）」
# EXPR_DONT_UNDERSTAND = (
#     "出现这句话说明有bug..."
# )
#
#
# # 注册一个仅内部使用的命令，不需要 aliases
# # @on_command('ai_chat2')
# async def ai_chat(session: CommandSession):
#     # 获取可选参数，这里如果没有 message 参数，message 变量会是 None
#     message = session.state.get('message')
#     # print(message, type(message))
#     # 通过封装的函数获取腾讯智能机器人机器人的回复
#     reply = await call_tencent_TextProcess_api(session, message)
#     if reply:
#         # 如果调用腾讯智能机器人成功，得到了回复，则转义之后发送给用户
#         # 转义会把消息中的某些特殊字符做转换，避免将它们理解为 CQ 码
#         await session.send(escape(reply))
#     else:
#         # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取腾讯智能机器人回复时的「表达」
#         # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
#         await session.send(render_expression(EXPR_DONT_UNDERSTAND))
#
#
# def call_tencent_TextProcess_api(text: Optional[str]) -> Optional[str]:
#     cred = credential.Credential('AKID1qRnulPoxrVyB9sMcdO0MTKxLUN3VifN',
#                                  'GI5dw0oNhmcCWbR1MTN1QZT9ZkhPr41j')
#     httpProfile = HttpProfile()
#     httpProfile.endpoint = "tbp.tencentcloudapi.com"
#
#     clientProfile = ClientProfile()
#     clientProfile.httpProfile = httpProfile
#     client = tbp_client.TbpClient(cred, "", clientProfile)
#
#     req = models.TextProcessRequest()
#     params = {
#         "BotId": "c8451fa1-d2d4-4974-9e76-1e8b99bfcc49",
#         "BotEnv": "release",
#         "TerminalId": "AI_001",
#         "InputText": text
#     }
#     req.from_json_string(json.dumps(params))
#
#     resp = client.TextProcess(req).to_json_string()
#     print(type(resp))
#     resp_payload = json.loads(resp)
#     print(type(resp_payload))
#     print(resp_payload["ResponseMessage"]["GroupList"][0].get("Content"))
# call_tencent_TextProcess_api("我不开心")
