# 示例10-7：包的导入
    # 一、 import 包名.模块名 as 别名
import admin.my_admin as a
a.info()
# 包导入会自动执行init文件的代码

    # 二、 from 包名 import 模块名 as 别名
from admin import  my_admin as b
b.info()
# 包导入时只会执行一次init文件的代码

    # 三、 from 包名.模块名 import 变量/函数/类
from admin.my_admin import info
info()

    # 四、 from 包名.模块名 import *
from admin.my_admin import  *
print(name)
 

