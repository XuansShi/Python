# 示例10-2：模块的导入
# 一、import 模块名称
import my_info

# 二、import 模块名称 as 别名
import my_info as mi

# 三、from 模块名 import 变量/函数/类/*
from my_info import  info
info()

# 通配符
from my_info import  *


# 四、同时导入多个模块
import math,time,random,sys,os
    #如果两个模块中有同名的函数，后导入模块的函数会将先导入的覆盖。这样就只能用模块名称点出调用





