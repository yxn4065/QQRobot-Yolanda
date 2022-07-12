# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/20 23:02 
# @IDE : PyCharm(2022.1) Python3.9.12
import os
import platform

if __name__ != '__main__':
    plat = platform.system().lower()
    if plat == 'windows':
        print('当前环境:windows系统')
    elif plat == 'linux':
        print('当前环境:linux系统')

    if os.name == 'posix':
        print(' 开始执行语句:pip3 install -U quart')
        os.system('pip3 install -U quart')  # 解决报错问题
        print("pip3 install -U quart 执行成功!")
