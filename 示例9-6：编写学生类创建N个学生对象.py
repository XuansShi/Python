# 示例9-6：编写学生类创建N个学生对象
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

# 根据Student类创建N多个对象
stu1 = Student('刘备',34)
stu2 = Student("关羽",35)

print(type(stu1))
print(type(stu2))

Student.school = "南山敬老院"  # 类属性使用类名点出调用

# 将学生对象存储到列表中
lst= [ stu1, stu2]
for item in lst:
    item.show()




















