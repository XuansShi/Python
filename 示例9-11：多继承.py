# 示例9-11：多继承
# 创建多个父类
class FatherA():
    def __init__(self,name):
        self.name = name

    def showA(self):
        print("父类A中的方法showA")

class FatherB():
    def __init__(self,name):
        self.name = name

    def showB(self):
        print("父类B中的方法showB")

# 多继承
class Son(FatherA,FatherB):
    def __init__(self,name,age,gender):
        # 有多个父类就不能使用super调用父类的成员了，应该使用类名来进行区分
        FatherA.__init__(self,name)
        FatherB.__init__(self,name)
        self.gender=gender

# 实例化
son = Son('xs',18,'n') #调用Son类中的__init__执行

son.showA()
son.showB()

