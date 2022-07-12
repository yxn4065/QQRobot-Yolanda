# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/5/16 17:24 
# @IDE : PyCharm(2022.1.1) Python3.9.12

import requests
from nonebot import CommandSession, on_command

# 使用帮助
__plugin_name__ = '致远语录'
__plugin_usage__ = r"""
超强语录接口 -奇远api

发送 "致远语录" 获取内容,支持指定类型~默认为2004(文学)

{"1001": "土味情话", 
"1002": "精神语录", 
"1003": "网易云热评", 
"1004": "成人笑话",
"1005": "奇葩对话", 
"1006": "舔狗日记", 
"1007": "毒鸡汤", 
"1009": "骂人宝典",
"2001": "动画", 
"2002": "漫画", 
"2003": "游戏", 
"2004": "文学", 
"2005": "原创", 
"2006": "来自网络",
"2007": "其他", 
"2008": "影视",
"2009": "诗词", 
"2010": "网易云",
"2011": "哲学", 
"2012": "抖机灵"}
获取指定内容请发送 "致远语录 对应编号"
"""
EXPR_DONT_UNDERSTAND = f'>>出现这句话说明该插件{__file__}有问题,建议进行排查!'


@on_command('Qiyuan_quotations', aliases="致远语录", only_to_me=False)
async def handle_first_receive(session: CommandSession):
    id = session.current_arg_text.strip()
    # 默认直接返回2004
    if not id:
        result = await Qiyuan_quotations()
        await session.send(result)
    else:
        result = await Qiyuan_quotations(int(id))
        await session.send(result)


async def Qiyuan_quotations(id=2004):
    # style = {"1001": "土味情话", "1002": "精神语录", "1003": "网易云热评", "1004": "成人笑话",
    #              "1005": "奇葩对话", "1006": "舔狗日记", "1007": "毒鸡汤", "1009": "骂人宝典",
    #              "2001": "动画", "2002": "漫画", "2003": "游戏", "2004": "文学", "2005": "原创",
    #              "2006": "来自网络", "2007": "其他", "2008": "影视", "2009": "诗词", "2010": "网易云",
    #              "2011": "哲学", "2012": "抖机灵"}
    try:
        # id = style["2011"]
        # print(id)
        # print(list(style.keys())[list(style.values()).index('抖机灵')])  # 由字典的值得到键的值
        url = "https://api.oddfar.com/yl/q.php?c={}&encode=txt".format(id)
        response = requests.get(url).text
        # print(r)
        return response

    except Exception as e:
        return f"出错啦:{e}"
