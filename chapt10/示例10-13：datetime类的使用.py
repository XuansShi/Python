# 示例10-13：datetime类的使用
from datetime import datetime #从datetime模块中导入datetime类

# 一 datetime.datetime
dt=datetime.now()
print("当前系统时间为",dt)

#datetime是一个类，手动创建这个类的对象
dt2 = datetime(2099,8,8,20,1,0)
print("dt2的数据类型：",type(dt2),"表示的时间为",dt2)
print("年 月 日 时 分 秒",dt2.year,dt2.month,dt2.day,dt2.hour,dt2.minute,dt2.second)


#比较两个datetime类型对象的大小
labor_day = datetime(2099,5,1,0,0,0)
national_day = datetime(2099,10,1,0,0,0)
print("2099年5月1日 比 2099年10月1日 早吗？",labor_day<national_day)


#datetime类型与字符串进行转换
    #datetime转字符串
nowdt=datetime.now()
nowdt_str=nowdt.strftime("%Y%m%d%H%M%S")
print("nowdt数据类型",type(nowdt))
print("nowdt_str数据类型",type(nowdt_str))
    #字符串转datetime
str_datetime="2028年8月8日 20点8分"
dt3=datetime.strptime(str_datetime,"%Y年%m月%d日 %H点%M分")
print("str_datetime数据类型",type(str_datetime))
print("dt3数据类型",type(dt3))







