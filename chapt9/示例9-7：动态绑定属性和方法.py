# 示例9-7：动态绑定属性和方法
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

# 根据Student类创建2个对象
stu1 = Student('刘备',34)
stu2 = Student("关羽",35)
print(stu1.name,stu1.age)
print(stu2.name,stu2.age)



# 为stu2动态绑定一个实例属性
stu2.gender = "男"
print(stu2.name,stu2.age,stu2.gender)

# 为stu2动态绑定一个方法
def introduce():
    print("为stu2动态绑定一个方法")

stu2.fun = introduce() # 绑定： 把方法introduce赋值给函数fun。注意fun不能加小括号，不然就调用了
    #调用stu2的方法fun()
stu2.fun()


