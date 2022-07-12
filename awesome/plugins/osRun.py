# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/22 11:59 
# @IDE : PyCharm(2022.1) Python3.9.12

import os

from nonebot import on_command, CommandSession
from nonebot import on_natural_language, NLPSession, IntentCommand


# 使用帮助
# __plugin_name__ = '执行系统命令(限超级用户)'
# __plugin_usage__ = r"""
# 后台操作
# """

@on_command('更新软件', permission=lambda s: s.is_superuser)
async def _(session: CommandSession):
    os.system('yum update')
    await session.send('已更新系统软件!')


@on_command('Run', permission=lambda s: s.is_superuser)
async def _(session: CommandSession):
    try:
        hash = "****"
        # 取得消息的内容，并且去掉首尾的空白符
        cmd = session.current_arg_text.strip("Run")
        if not cmd:
            cmd = (await session.aget(prompt='请输入你需要执行的指令:')).strip()
            # 如果用户只发送空白符，则继续询问
            while not cmd:
                cmd = (await session.aget(prompt='指令为空,请重新输入')).strip()

        password = await session.aget("接收指令成功!请输入哈希密码4进行核对:")
        if password != hash:
            await session.send(f'密码校验不成功,指令{cmd}执行失败!')
        else:
            res = os.system(cmd)
            await session.send(f'指令{cmd}执行完毕!,结果为:{res}')
    except Exception as e:
        await session.send(f'发生错误:{e}')


@on_natural_language(keywords={'Run'}, permission=lambda s: s.is_superuser)
async def _(session: NLPSession):
    return IntentCommand(90.0, 'Run')
