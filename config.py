# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 14:43 
# @IDE : PyCharm(2022.1) Python3.9.12

import re
from nonebot.default_config import *
from datetime import timedelta

group_Test = "903475050"  # Test群号
# 664988568 情书

# debug模式,默认开启
# DEBUG = False

# 配置超级用户
SUPERUSERS = {1912047718}

# 配置命令的起始字符
# COMMAND_START = {'', '/', '!', '／', '！'}
COMMAND_START = ['', re.compile(r'[/!]+')]

# 配置监听的 IP 和端口
HOST = '127.0.0.1'  # '0.0.0.0'
PORT = 8081

# 设置专属名称
NICKNAME = {'Yolanda' '尤兰达', '小Yo', '小幽', 'yoyo', '悠悠', '小蛇', '小悠', '小yo'}

# 腾讯云智能对话平台接入
TENCENT_BOT_SECRET_ID = '请自己手动去获取密钥'
TENCENT_BOT_SECRET_KEY = '请自己手动去获取密钥'

# 这里 IP 和端口应与 go-cqhttp 配置中的 `host` 和 `port` 对应
API_ROOT = 'http://127.0.0.1:5700'

# alapl官网及密钥
ALAPI_URL = "https://www.alapi.cn/"
ALAPI_TOKEN = "token=请自己手动去获取密钥"

# 设置过期超时为 2 分钟，即用户 2 分钟不发消息后，会话将被关闭。
SESSION_EXPIRE_TIMEOUT = timedelta(minutes=1)

# 命令参数验证失败（验证器抛出 ValidateError 异常）、且验证器没有指定错误信息时，默认向用户发送的错误提示。
DEFAULT_VALIDATION_FAILURE_EXPRESSION = '你发送的内容格式不太对呢，请检查一下再发送哦～'

# 命令参数验证失败达到 MAX_VALIDATION_FAILURES 次之后，向用户发送的提示。
TOO_MANY_VALIDATION_FAILURES_EXPRESSION = (
    '你输错太多次啦，需要的时候再叫我吧',
    '你输错太多次了，建议先看看使用帮助哦～',
)
