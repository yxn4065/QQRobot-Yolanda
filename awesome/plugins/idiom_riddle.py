# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 22:09 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '成语猜猜猜'
__plugin_usage__ = r"""
成语谜语猜猜猜

发送 "成语谜语" 获得题目 等你来挑战!
发送 "成语猜猜猜" 获得图片题目 等你来挑战!
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('idiom_riddle', aliases="成语谜语", only_to_me=True)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    puzzle, answer = await idiom_riddle()
    # 向用户发送结果
    an = (await session.aget(prompt=puzzle)).strip()
    if an == answer:
        await session.send("恭喜你,回答正确!答案: " + answer)
    else:
        await session.send("回答错误了哦~再接再厉!\n答案: " + answer)


async def idiom_riddle():
    try:
        url = "https://v2.alapi.cn/api/riddle/random"
        payload = "token=请自己手动去获取密钥&type=chengyumiyu"
        headers = {'Content-Type': "application/x-www-form-urlencoded"}
        response = requests.request("POST", url, data=payload, headers=headers).json()
        puzzle = "请根据题目答一成语:\n" + response['data']['content']
        answer = response['data']['answer']
        return puzzle, answer

    except Exception as e:
        return f"出错啦:{e}"


@on_command('idiom_riddle_img', aliases=("成语猜猜猜", "看图猜成语",), only_to_me=True)
async def handle_first_receive(session: CommandSession):
    # 获取数据
    message, answer, res = await idiom_riddle_img()
    # 向用户发送结果
    an = (await session.aget(prompt=message)).strip()
    if an == answer:
        await session.send("恭喜你,回答正确!答案: " + answer + "\n" + res)
    else:
        await session.send("回答错误了哦~再接再厉!\n答案: " + answer + "\n" + res)


async def idiom_riddle_img():
    try:
        url = "http://api.weijieyue.cn/api/tupian/ktcy.php"
        r = requests.get(url).json()
        x = r["data"][0]
        # print(x.get('image'))
        # print(x.get('name'))
        # print(x.get('interpret'))
        # print(x.get('provenance'))
        # img = "[CQ:image,file=" + str(x.get('image')) + ",]"
        message = [
            {
                "type": "text",
                "data": {
                    "text": "请根据图片答一成语:\n"
                }
            }, {
                "type": "image",
                "data": {
                    "file": str(x.get('image')),
                }
            }
        ]
        answer = x.get('name')
        paraphrase = x.get('interpret')
        provenance = x.get('provenance')
        res = "解释: " + paraphrase + "\n" + "出处: " + provenance + "\n"

        return message, answer, res

    except Exception as e:
        return f"出错啦:{e}"
