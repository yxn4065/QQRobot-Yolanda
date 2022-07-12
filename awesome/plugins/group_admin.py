# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 20:47 
# @IDE : PyCharm(2022.1) Python3.9.12

from nonebot import on_notice, on_request, RequestSession, NoticeSession


# 将函数注册为群请求处理器
@on_request('group')
async def _(session: RequestSession):
    # 判断验证信息是否符合要求
    if '图灵测试' in session.event.comment:
        # 验证信息正确，同意入群
        await session.approve()
        return
    # 验证信息错误，拒绝入群
    await session.reject('请说暗号')


# 将函数注册为群成员增加通知处理器
@on_notice('group_increase')
async def _(session: NoticeSession):
    # 发送欢迎消息
    if session.event.group_id in ['903475050', '638220483', '664988568']:
        await session.send('欢迎新朋友～\n我是机器人Yolanda,没事找我聊天吧~')
# session.event.group_id 预先判断一下是不是你想发送的群否则机器人所在的任何群有新成员进入它都会欢迎.
