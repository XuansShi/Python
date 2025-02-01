# 示例10-15：爬取景区的天气预报
import requests # 导入爬虫对应的模块
import re # 导入正则表达式对应的模块
url="https://www.weather.com.cn/weather/101200101.shtml" #爬虫打开的浏览器上的网页
response = requests.get(url) # 打开浏览器，打开网址，返回响应对象

print(response.text) # 打印响应对象response的text信息
    # 直接打印出现一堆英文，可以设置一下编码格式

response.encoding = "utf-8"# 编码格式改为utf-8
print(response.text)

# 但是直接打印的是http信息，可以使用正则表达式进行筛选：
# 可以直接查找相关信息以获得模式字符串
'''
比如说运行上面的代码后，在中断里按ctrl+F，然后查找“三亚”，有：

<span class="name">三亚</span>
<span class="weather">多云</span>
<span class="wd">24/15℃</span>
<span class="zs">适宜</span>

'''

# 提取：
city = re.findall('<span class="name">([\u4e00-\u9fa5]*)</span>',response.text)# 习：任意长度的中文这样写：[\u4e00-\u9fa5]*
weather = re.findall('<span class="weather">([\u4e00-\u9fa5]*)</span>',response.text)
wd = re.findall('<span class="wd">(.*)</span>',response.text)# .*  代表匹配任意字符一次或多次
zs = re.findall('<span class="zs">([\u4e00-\u9fa5]*)</span>',response.text)
print(city)
print(weather)
print(wd)
print(zs)
print()

# 打包数据
lst=[]
for a,b,c,d in zip(city,weather,wd,zs):
    lst.append([a,b,c,d]) #列表里插列表

    # 遍历打包好的列表
for item in lst:# 列表lst里有7个元素，它们都是有4个元素的列表
    print(item)















