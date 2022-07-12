# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 18:49 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '狗屁不通文章生成'
__plugin_usage__ = r"""
根据你的题目生成一篇指定字数的“论文”，仅供恶搞！

发送 "狗屁不通文章生成 文章标题" 获取内容~
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('bullshit_article_generation', aliases="狗屁不通文章生成")
async def handle_first_receive(session: CommandSession):
    title = session.current_arg_text.strip()
    if not title:
        title = (await session.aget(prompt='请输入你想生成的文章标题:')).strip()
        # 如果用户只发送空白符，则继续询问
        while not title:
            title = (await session.aget(prompt='文章标题不能为空呢，请重新输入')).strip()
    # 获取数据
    result = await bullshit_article_generation(title)
    # 向用户发送结果
    await session.send(result)


async def bullshit_article_generation(title: str):
    try:
        url = "https://api.pingping6.com/tools/bullshit/index.php?title={}&num=1500".format(title)
        r = requests.get(url).json()
        # print(r['article'].replace("'\u3000\u3000", "  ").replace("\n", '\n'))
        res = r['article'].replace("'\u3000\u3000", "  ").replace("\n", '\n')
        return res

    except Exception as e:
        return f"出错啦:{e}"
