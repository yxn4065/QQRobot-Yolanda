# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 19:32 
# @IDE : PyCharm(2022.1.1) Python3.9.12

from nonebot import CommandSession, on_command
from nonebot import IntentCommand, NLPSession, on_natural_language

# 使用帮助
__plugin_name__ = ''
__plugin_usage__ = r"""


自己设置一些对话,以较高置信度返回~
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('conversation_1', aliases=("你叫什么名字?", "你是谁?", "你叫什么名字"))
async def handle_first_receive(session: CommandSession):
    # 获取数据
    res = "我叫 Yolanda(尤兰达),一株高贵的紫罗兰~~~\n" \
          "你可以叫我'小yo', 'yoyo', '小幽', '悠悠','幽幽'...\n" \
          "让我来逗你开心吧~"
    # 向用户发送结果
    await session.send(res)


@on_command('conversation_2', aliases='杨雪南')
async def handle_first_receive(session: CommandSession):
    # 获取数据
    res = "'雪南'是一个努力成长中的Python爱好者~也是我的主人,不知你找他有有什么事情呢?"
    # 向用户发送结果
    await session.send(res)


@on_natural_language(keywords={'名字', '杨雪南'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'conversation_1')


@on_natural_language(keywords={'杨雪南', '雪南'})
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(90.0, 'conversation_2')
