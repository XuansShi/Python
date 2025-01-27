# 示例10-12：time模块的使用
import time

# 一 time()  获取当前时间戳
now = time.time()
print(now)

# 二 localtime(sec)
print(time.localtime())
obj = time.localtime(60)
print(type(obj))
print("年份",obj.tm_year)
print("月份",obj.tm_mon)
print("日期",obj.tm_mday)
print("时",obj.tm_hour)
print("分",obj.tm_min)
print("秒",obj.tm_sec)
print("星期",obj.tm_wday)  # 0到6
print("今年的多少天",obj.tm_yday)


# 三 ctime()
print(time.ctime())


# 四 strftime()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))  #格式化为 年月日时分秒
print("%B月份的名称",time.localtime(time.time()))
print("%A星期的名称",time.localtime(time.time()))


# 五 strptime()
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

# 六 sleep(sec)
time.sleep(10) #程序休眠十秒






