# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 21:06 
# @IDE : PyCharm(2022.1) Python3.9.12
import time
from datetime import datetime

import nonebot
import pytz

import requests
from aiocqhttp.exceptions import Error as CQHttpError
import datetime
from apscheduler.triggers.date import DateTrigger  # 一次性触发器
from apscheduler.triggers.cron import CronTrigger  # 定期触发器
from apscheduler.triggers.interval import IntervalTrigger  # 间隔触发器
from nonebot import CommandSession, on_command, scheduler

# 使用帮助
# __plugin_name__ = '设置定时任务(限超级用户)'
# __plugin_usage__ = r"""
# 后台操作
# """

bot = nonebot.get_bot()
now = datetime.now(pytz.timezone('Asia/Shanghai'))


# @nonebot.scheduler.scheduled_job('interval', minutes=10) 每十分钟执行一次任务
# @nonebot.scheduler.scheduled_job('cron', hour='12', minute=0, second=0)
# async def _():
#     try:
#         await bot.send_group_msg(group_id=903475050,
#                                  message=f'现在{now.hour}点整啦！')
#     except CQHttpError:
#         pass


@nonebot.scheduler.scheduled_job('date', run_date=datetime(2023, 1, 1, 0, 0),
                                 # timezone=None,
                                 )
async def _():  # 一次性任务
    await bot.send_group_msg(message="2023，新年快乐！")


@nonebot.scheduler.scheduled_job(
    'cron',
    # year=None,
    # month=None,
    # day=None,
    # week=None,
    day_of_week="mon,tue,wed,thu,fri",
    hour=8,
    # minute=None,
    # second=None,
    # start_date=None,
    # end_date=None,
    # timezone=None,
)
async def _():  # 定期任务
    await bot.send_group_msg(group_id=903475050, message="起床啦！")


def check_new_item():
    pass


@nonebot.scheduler.scheduled_job(
    'interval',
    # weeks=0,
    # days=0,
    # hours=0,
    minutes=5,
    # seconds=0,
    # start_date=time.now(),
    # end_date=None,
)
async def _():  # 间隔任务
    pass
    # has_new_item = check_new_item()
    # if has_new_item:
    #     await bot.send_group_msg(group_id=123456,message="XX有更新啦！")


@on_command('赖床')  # 动态的计划任务
async def _(session: CommandSession):
    await session.send('我会在5分钟后再喊你')

    # 制作一个“5分钟后”触发器
    delta = datetime.timedelta(minutes=5)
    trigger = DateTrigger(run_date=datetime.datetime.now() + delta)

    # 添加任务
    scheduler.add_job(
        func=session.send,  # 要添加任务的函数，不要带参数
        trigger=trigger,  # 触发器
        args=('不要再赖床啦！卷起来,今天不学习,明天变垃圾!!!',),  # 函数的参数列表，注意：只有一个值时，不能省略末尾的逗号
        # kwargs=None,
        misfire_grace_time=60,  # 允许的误差时间，建议不要省略
        # jobstore='default',  # 任务储存库，在下一小节中说明
    )


# ##全天问候实列
# 获取当前是星期几
def week_now():
    week_list = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    return week_list[time.localtime().tm_wday]


def word_now():
    word_list = ['美好的一周从周一开始~\n早上好呀~~\n',
                 '今天是周二~\n又是元气满满一天~~\n',
                 '每天起床第一句,先给自己打个气~\n周三早上好~~\n',
                 '今天是周四~\n不要忘记好好学习噢~~\n',
                 '今天是周五~\n宜: 学习和刷题~~'
                 '早上好~~\n周六快乐,要开心呀~~\n',
                 '今天是周日~\n不要忘记学习和刷题复习噢~\n']
    return word_list[time.localtime().tm_wday]


# MC酱的表情包
url_mc = 'https://api.ixiaowai.cn/mcapi/mcapi.php'
# 风景壁纸
url_scenery = 'https://api.ixiaowai.cn/gqapi/gqapi.php'
requests.packages.urllib3.disable_warnings()


def get_mc(url):
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/93.0.4577.63 Safari/537.36'
    }
    res = requests.get(url, headers=headers, verify=False)
    return res.url


# 定时消息 (全天)
@scheduler.scheduled_job('cron', day_of_week='0-6', hour=8, minute=30)
async def demo():
    # mybot = nonebot.get_bot()
    group_id = int(bot.config.group_Test)
    # group_id_1 = int(driver.config.group_id_1)
    msg = word_now()
    message = [
        {
            "type": "text",
            "data": {
                "text": msg
            }
        },
        {
            "type": "image",
            "data": {
                "file": get_mc(url_mc),
            }
        }
    ]
    await bot.send_group_msg(group_id=group_id, message=message)


# 设置定时发送
@scheduler.scheduled_job('paper', day_of_week='0-6', hour=8, minute=00)
async def demo():
    bot = nonebot.get_bot()
    group_id = int(bot.config.group_Test)
    url = "https://v2.alapi.cn/api/zaobao"
    payload = "token=请自己手动去获取密钥&format=json"
    headers = {'Content-Type': "application/x-www-form-urlencoded"}
    response = requests.request("POST", url, headers=headers, data=payload).json()
    mes = response['data']['date'] + "\n"
    mes += 'head_image: ' + response['data']['head_image'] + "\n"
    mes += 'image: ' + response['data']['image'] + "\n" + '早报内容: \n'
    for i in response['data']['news']:
        print(i)
        mes += i
    mes += "\n" + response['data']['weiyu']
    message = [
        {
            "type": "text",
            "data": {
                "text": mes
            }
        },
        {
            "type": "image",
            "data": {
                "file": response['data']['head_image'],
            }
        }
    ]
    await bot.send_group_msg(group_id=group_id, message=message)
