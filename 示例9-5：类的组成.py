# 示例9-5：类的组成
class Student:
# 类属性：定义在类中，方法外的变量
    school= "北海幼儿园"

# 实例属性
    # __init__初始化方法
    def __init__(self,xm,age):# 必须这样写：  __init__
        # xm,age是方法的参数，是局部变量,作用域是__init__方法
        self.name = xm # 等号左侧的self.name是实例属性，xm是局部变量
        self.age = age

    # 定义在类中的函数称为方法，自带一个参数self
    def show(self):
        print(self.name, self.age)#像__init__方法中的变量xm是局部变量，只能在__init__方法中使用，而实例属性可以在整个类中使用

    # 静态方法
        # 静态方法不会自带self
    @staticmethod
    def sm():
        print("在静态方法中，同样不能调用 实例属性 和 实例方法")

    # 类方法
        # 类方法会自带一个cls
    @classmethod
    def cm(cls):#cls 就是 class的缩写
        print("在类方法中，同样不能调用 实例属性 和 实例方法")


# 实例化
stu = Student("xs",18) # 在__init__方法中有两个参数xm和age，所以需要写两个参数；而self是自带的参数，无需传入

# 实例属性 使用 对象名 点出调用
print(stu.name,stu.age)
# 实例方法 使用 对象名 点出调用
stu.show()

# 静态方法(@staticmethod修饰的方法)，使用 类名 点出调用
Student.sm()
# 类方法（@classmethod修饰的方法），使用 类名 点出调用
Student.cm()


# 静态方法、类方法、类属性 使用类名调用
# 和实例有关的 使用对象名调用
