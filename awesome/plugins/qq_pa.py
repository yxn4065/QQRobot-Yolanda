# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/20 22:39 
# @IDE : PyCharm(2022.1.1) Python3.9.12
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = 'qq丢人爬'
__plugin_usage__ = r"""
发送对方QQ号,给你返回~(小心挨打)

发送"qq爬 qq号"获取~~~爬呀,一起爬
发送"qq丢 qq号"获取~~~丢呀,一起丢
发送"qq赞 qq号"获取~~~赞呀,你最棒
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('qq_pa', aliases=('qq爬', 'QQ爬'), only_to_me=False)
async def weather(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    qqid = session.current_arg_text.strip()
    if not qqid:
        qqid = (await session.aget(prompt='你想安排谁爬呢？请输入一个QQ号')).strip()
        # 如果用户只发送空白符，则继续询问
        while not qqid:
            qqid = (await session.aget(prompt='安排谁爬呢？QQ号不能为空呢，请重新输入')).strip()

    res = await qq_pa(int(qqid))

    await session.send(res)


async def qq_pa(qqid):
    try:
        url = "http://api.weijieyue.cn/api/tupian/pa.php?qq={}".format(qqid)
        res = "[CQ:image,file=" + url + ",]"
        return res

    except Exception as e:
        return f"出错啦:{e}"


@on_command('qq_diu', aliases=('qq丢', 'QQ丢'), only_to_me=False)
async def weather(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    qqid = session.current_arg_text.strip()
    if not qqid:
        qqid = (await session.aget(prompt='你想安排谁爬呢？请输入一个QQ号')).strip()
        # 如果用户只发送空白符，则继续询问
        while not qqid:
            qqid = (await session.aget(prompt='安排谁爬呢？QQ号不能为空呢，请重新输入')).strip()

    res = await qq_diu(int(qqid))

    await session.send(res)


async def qq_diu(qqid):
    try:
        url = "http://api.weijieyue.cn/api/tupian/diu.php?qq={}".format(qqid)
        res = "[CQ:image,file=" + url + ",]"
        return res

    except Exception as e:
        return f"出错啦:{e}"


@on_command('qq_zan', aliases=('qq赞', 'QQ赞', "q赞"), only_to_me=False)
async def weather(session: CommandSession):
    # 取得消息的内容，并且去掉首尾的空白符
    qqid = session.current_arg_text.strip()
    if not qqid:
        qqid = (await session.aget(prompt='你想安排谁爬呢？请输入一个QQ号')).strip()
        # 如果用户只发送空白符，则继续询问
        while not qqid:
            qqid = (await session.aget(prompt='安排谁爬呢？QQ号不能为空呢，请重新输入')).strip()

    res = await qq_zan(int(qqid))

    await session.send(res)


async def qq_zan(qqid):
    try:
        url = "http://api.weijieyue.cn/api/tupian/zan.php?qq={}".format(qqid)
        res = "[CQ:image,file=" + url + ",]"
        return res

    except Exception as e:
        return f"出错啦:{e}"
