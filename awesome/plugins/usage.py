# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 21:13 
# @IDE : PyCharm(2022.1) Python3.9.12

import nonebot
from nonebot import on_command, CommandSession


# 插件的 name 属性（plugin.name）用于获得插件模块的 __plugin_name__ 特殊变量的值
# 插件的 usage 属性（plugin.usage）用于获得插件模块的 __plugin_usage__ 特殊变量的值

@on_command('usage', aliases=['help', '使用帮助', '帮助', '使用方法', '使用教程', '说明', "使用说明"],
            only_to_me=True)
async def _(session: CommandSession):
    # 函数用于获取所有已经加载的插件，注意，由于可能存在插件没有设置__plugin_name__
    # 变量的情况，插件的名称有可能为空，因此需要过滤一下
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    arg = session.current_arg_text.strip().lower()
    if not arg:
        # 如果用户没有发送参数，则发送功能列表
        await session.send(
            '小Yo现在支持的功能有：\n\n' + '\n'.join(p.name for p in plugins) +
            "\n\n温馨提示:如需查看详细内容,请发送  '使用帮助 功能名称' 获取说明~ ")
        return

    # 如果发了参数则发送相应命令的使用帮助
    for p in plugins:
        if p.name.lower() == arg:
            await session.send(p.usage)
