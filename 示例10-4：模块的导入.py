# 示例10-4：模块的导入
from my_info import *
from introduce import  *


# 导入模块中具有同名的变量和函数，后导入模块的函数会将先导入的覆盖。
    #如果不想覆盖，解决方案：使用import,使用模块中的函数或者变量时，模块名打点调用
import my_info
import introduce


my_info.info()
introduce.info()


