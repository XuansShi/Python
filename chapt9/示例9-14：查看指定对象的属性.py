# 示例9-14：查看指定对象的属性
class Person(object):
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f'我叫{self.name},年龄{self.age}岁')

# 实例化
per = Person("吉良吉影",33)

print(dir(per))# 查看per的属性

print(per)# 自动调用了__str__方法，返回对象的描述

















