# 示例9-12：方法重写
# 创建父类Person类
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

# Student类
class Student(Person):
    # 编写初始化的方法
    def __init__(self,name,age,stuno):
        super().__init__(name,age)
        self.stuno=stuno

    def show(self):
        print("编写子类独有的属性。Student子类重写父类的show方法")
        print("子类有优先调用子类的，没有再在父类里找")


# Doctor类
class Doctor(Person):
    # 编写初始化的方法
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department=department

    def show(self):
        #super().show() #习：调用父类的show方法。在子类重写父类方法时可写可不写
        print("Doctor子类重写父类show方法。",f'大家好，我叫{self.name},我今年{self.age}岁，在{self.department}上班')



# 创建子类对象
stu = Student('xs',18,"1101")
doc = Doctor('sss',23,"外科")
stu.show()
doc.show()









