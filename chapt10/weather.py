# 示例10-17：封装 爬取景区的天气预报 文件
import requests
import re

# 爬取 函数
def get_html():
    url="https://www.weather.com.cn/weather/101200101.shtml"
    response = requests.get(url)
    response.encoding = "utf-8"
    return response.text

# 解析，并且打包 函数
def parse_html(html_str):
    city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',html_str)
    weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',html_str)
    wd = re.findall('<span class="wd">(.*)</span>',html_str)
    zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',html_str)
    lst=[]
    for a,b,c,d in zip(city,weather,wd,zs):
        lst.append([a,b,c,d])
    return lst















