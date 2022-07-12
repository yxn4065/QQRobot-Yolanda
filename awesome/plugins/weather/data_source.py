# -*- coding: utf-8 -*-
# @Author : yxn
# @Date : 2022/4/17 15:07 
# @IDE : PyCharm(2022.1) Python3.9.12

import json
import requests


async def get_weather_of_city(city: str) -> str:
    data = await get_weather_information(city)
    if data is None:
        data = await get_weather(city)  # 换用另一个api
    return f'查询到{city}的天气信息如下:\n{data}'


async def get_weather_information(city):
    data = "天气" + city
    # 发送requests请求并处理数据
    response = requests.get("http://api.qingyunke.com/api.php?key=free&appid=0&msg={}".format(data))
    if response.status_code != 200:
        return None
    res = response.json()
    ret = res["content"]
    result = ret.replace("{br}", "\n")
    return result


async def get_weather(city: str):
    import urllib
    import gzip
    cityname = city
    url = 'http://wthrcdn.etouch.cn/weather_mini?city=' + urllib.parse.quote(
        cityname)  # 访问的url，其中urllib.parse.quote是将城市名转换为url的组件
    weather_data = urllib.request.urlopen(url).read()  # 发出请求并读取到weather_data
    weather_data = gzip.decompress(weather_data).decode('utf-8')  # 以utf-8的编码方式解压数据
    weather_dict = json.loads(weather_data)  # 将json数据转化为dict数据
    if weather_dict.get('desc') == 'invilad-citykey':
        return f"抱歉,小YO似乎木有查询到这个地方的天气哎..."

    elif weather_dict.get('desc') == 'OK':
        forecast = weather_dict.get('data').get('forecast')
        startoday = '城市：' + weather_dict.get('data').get('city') + '\n' \
                    + '日期：' + forecast[0].get('date') + '\n' \
                    + '温度：' + weather_dict.get('data').get('wendu') + '℃\n' \
                    + '高温：' + forecast[0].get('high') + '\n' \
                    + '低温: ' + forecast[0].get('low') + '\n' \
                    + '风向：' + forecast[0].get('fengxiang') + '\n' \
                    + '风力：' + forecast[0].get('fengli') + '\n' \
                    + '天气：' + forecast[0].get('type') + '\n' \
                    + '感冒：' + weather_dict.get('data').get('ganmao') + '\n'
        return startoday
