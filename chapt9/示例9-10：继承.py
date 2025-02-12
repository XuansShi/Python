# 示例9-10：继承
# 创建父类Person类
class Person:#默认继承了object
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

# Student类 继承 Person类
class Student(Person):
    # 编写初始化的方法
    def __init__(self,name,age,stuno):
        super().__init__(name,age) #调用父类的初始化方法，为子类的name和age赋值；super表示调用父类的属性和方法
        self.stuno=stuno

# Doctor类 继承 Person类      一个父类可以有N个子类
class Doctor(Person):
    # 编写初始化的方法
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department


# 创建子类对象
stu = Student('xs',18,"1101")
doc = Doctor('sss',23,"外科")
stu.show()
doc.show()

