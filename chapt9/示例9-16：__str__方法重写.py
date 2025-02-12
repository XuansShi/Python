# 示例9-16：__str__方法重写
class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return '这是一个Person类，具有name和age两个实例属性'

per = Person("xs",20)
print(per)# 直接输出对象名，自动调用__str__方法
print(per.__str__())# 手动调用__str__方法









