# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 13:37 
# @IDE : PyCharm(2022.1.1) Python3.9.12
import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '战力查询'
__plugin_usage__ = r"""
查询王者荣耀最低战力地区(默认安卓QQ区)

发送 "战力查询 英雄名称"获取~
其它区请访问 "https://jk.cxkf.cc/"自助查询~

有你有团有荣耀,上分上星上王者
"""

EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('combat_power_query', aliases=("战力查询", "查战力"))
async def handle_first_receive(session: CommandSession):
    hreo_name = session.current_arg_text.strip()
    if not hreo_name:  # 默认发送当天内容
        hreo_name = (await session.aget(prompt='你想查询哪个英雄的最低战力呢？')).strip()
        # 如果用户只发送空白符，则继续询问
        while not hreo_name:
            hreo_name = (await session.aget(prompt='要查询的英雄名称不能为空呢，请重新输入')).strip()

    result = await combat_power_query(hreo_name)
    link = "[CQ:share,url=https://jk.cxkf.cc/,title=王者荣耀战力查询聚合]"
    await session.send(result)
    await session.send(link)


async def combat_power_query(hreo_name, tp="qq"):
    try:
        url = "https://jk.cxkf.cc/api_select.php?hero={}&type={}".format(hreo_name, tp)
        r = requests.get(url).json()
        r = requests.get(url).json()
        res = "查询到信息如下:\n" + r['data']['alias'] + "\n"
        res += "区级:" + r['data']['area'] + " ===> " + r["data"]['areaPower'] + "\n"
        res += "市级:" + r['data']['city'] + " ===> " + r["data"]['cityPower'] + "\n"
        res += "省级:" + r['data']['province'] + " ===> " + r["data"]['provincePower'] + "\n"
        res += "最后更新:" + r['data']['updatetime'] + "\n"
        return res

    except Exception as e:
        return f"出错啦:{e}"
