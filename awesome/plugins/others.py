# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/15 18:14
# @IDE : PyCharm(2022.1.1) Python3.9.12

from jieba import posseg
from nonebot import NLPSession, on_natural_language, IntentCommand

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = ''
__plugin_usage__ = r"""



"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('flag', aliases="口令")
async def handle_first_receive(session: CommandSession):
    # 获取数据
    result = await _()
    # 向用户发送结果
    await session.send(result)


async def _():
    try:

        return

    except Exception as e:
        return f"出错啦:{e}"


# city = session.current_arg_text.strip()
#     # 如果除了命令的名字之外用户还提供了别的内容，即用户直接将城市名跟在命令名后面，
#     # 则此时 city 不为空。例如用户可能发送了："天气 南京"，则此时 city == '南京'
#     # 否则这代表用户仅发送了："天气" 二字，机器人将会向其发送一条消息并且等待其回复
#     if not city:
#         city = (await session.aget(prompt='你想查询哪个城市的天气呢？')).strip()
#         # 如果用户只发送空白符，则继续询问
#         while not city:
#             city = (await session.aget(prompt='要查询的城市名称不能为空呢，请重新输入')).strip()

# on_natural_language 装饰器将函数声明为一个自然语言处理器
# keywords 表示需要响应的关键词，类型为任意可迭代对象，元素类型为 str
# 如果不传入 keywords，则响应所有没有被当作命令处理的消息
@on_natural_language(keywords={'未知'})
# @on_natural_language(keywords={'天气'},only_to_me=False)#不需要@直接进行响应
async def _(session: NLPSession):
    # 返回意图命令，前两个参数必填，分别表示置信度和意图命令名
    return IntentCommand(70.0, 'flag')


__plugin_name__ = ''
__plugin_usage__ = r"""
仅供开发人员进行使用

该插件用于测试,不实际上线,可用于隐藏指令,或者供开发人员使用
"""
