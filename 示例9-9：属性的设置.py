# 示例9-9：属性的设置
class Student:
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender # self.__gender是私有的实例属性

# 使用装饰器，将方法转成属性使用
    # @property
    @property
    def gender(self):# 名称和私有的实例属性一致
        return self.__gender# 转谁就返回谁

# 将gender属性设置为可写属性
    @gender.setter#  写法： 目标名称.setter
    def gender(self,value):# 名称必须和修改目标一致
        self.__gender = value # 给实例属性赋值

# 实例化
stu = Student("xs","n")

# 调用转换后得到的属性，并且查看
print(stu.name,"的性别是",stu.gender) # stu.gender会执行stu.gender()

# 尝试修改属性值
stu.gender = "男"
print(stu.name,"的性别是",stu.gender)














