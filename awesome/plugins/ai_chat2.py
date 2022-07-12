# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 19:08
# @IDE : PyCharm(2022.1) Python3.9.12
"""该模块调用的是对话机器人"""
import json
from typing import Optional
from aiocqhttp.message import escape
from nonebot import CommandSession, IntentCommand, on_command, on_natural_language
from nonebot.helpers import render_expression
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tbp.v20190627 import tbp_client, models

__plugin_name__ = '智能聊天Ⅱ'
__plugin_usage__ = r"""
智能聊天(腾讯智能对话平台tbp)

直接跟我聊天即可～
""".strip()

# 定义无法获取腾讯智能机器人回复时的「表达（Expression）」
EXPR_DONT_UNDERSTAND = (
    "出现这句话说明调用API失败...请联系开发人员"
)


# 注册一个仅内部使用的命令，不需要 aliases
@on_command('ai_chat2')
async def ai_chat(session: CommandSession):
    # 获取可选参数，这里如果没有 message 参数，message 变量会是 None
    message = session.state.get('message')
    # print(message, type(message))
    # 通过封装的函数获取腾讯智能机器人机器人的回复
    reply = await call_tencent_TextProcess_api(session, message)
    if reply:
        # 如果调用腾讯智能机器人成功，得到了回复，则转义之后发送给用户
        # 转义会把消息中的某些特殊字符做转换，避免将它们理解为 CQ 码
        await session.send(escape(reply))
    else:
        # 如果调用失败，或者它返回的内容我们目前处理不了，发送无法获取腾讯智能机器人回复时的「表达」
        # 这里的 render_expression() 函数会将一个「表达」渲染成一个字符串消息
        await session.send(render_expression(EXPR_DONT_UNDERSTAND))


@on_natural_language
async def _(session: CommandSession):
    # 以置信度 60.0 返回 ai_chat2 命令
    # 确保任何消息都在且仅在其它自然语言处理器无法理解的时候使用 ai_chat2 命令
    return IntentCommand(50.0, 'ai_chat2', args={'message': session.msg_text})


async def call_tencent_TextProcess_api(session: CommandSession, text: Optional[str]) -> Optional[str]:
    # 调用腾讯智能机器人的 API 获取回复
    if not text:
        return None
    try:
        cred = credential.Credential(session.bot.config.TENCENT_BOT_SECRET_ID,
                                     session.bot.config.TENCENT_BOT_SECRET_KEY)
        httpProfile = HttpProfile()
        httpProfile.endpoint = "tbp.tencentcloudapi.com"

        clientProfile = ClientProfile()
        clientProfile.httpProfile = httpProfile
        client = tbp_client.TbpClient(cred, "", clientProfile)

        req = models.TextProcessRequest()
        params = {
            "BotId": "c8451fa1-d2d4-4974-9e76-1e8b99bfcc49",
            "BotEnv": "release",
            "TerminalId": "AI_001",
            "InputText": text
        }
        req.from_json_string(json.dumps(params))

        resp = client.TextProcess(req).to_json_string()
        resp_payload = json.loads(resp)
        res = resp_payload["ResponseMessage"]["GroupList"][0].get("Content")
        return res

    except TencentCloudSDKException as err:
        print(err)
        return None
