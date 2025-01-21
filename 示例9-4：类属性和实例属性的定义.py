# 示例9-4：类属性和实例属性的定义
class Student:
    # 类属性：定义在类中，方法外的变量
    school= "北海幼儿园"

# 实例属性
    # 初始化方法
    def __init__(self,xm,age):# 必须这样写：  __init__
        # xm,age是方法的参数，是局部变量,作用域是__init__方法
        self.name = xm # 等号左侧的self.name是实例属性，xm是局部变量
        self.age = age
















