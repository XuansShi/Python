# 示例9-8：权限的控制
class Student():
    #首尾双下划线：特殊的方法
    def __init__(self,name,age,gender):
        self.gender=gender # self.gender 是普通的实例属性，public
        self._name=name # self._name 是protected受保护的，只能本类和子类访问
        self.__age=age # self.__age 是private私有的，只能类内访问

    # 单下划线-受保护的方法
    def _pr(self):
        print("权限：protected，只能本类和子类访问")

    # 双下划线-私有的方法
    def __pr2(self ):
        print("权限private，只能类内访问。但可以通过 对象名._类名__私有属性名 调用私有的实例属性  ； 对象名._类名__私有方法名()  调用私有的实例方法  ")

#实例化
stu = Student("xs",18,"n")

# 调用受保护的实例方法
stu._pr()

# 调用私有的实例属性和方法
    # 调用私有的实例属性
print(stu._Student__age)
    # 调用私有的实例方法
stu._Student__pr2()


# 补充：使用dir函数展示某对象所有的属性和方法
print(dir(stu))
    #输出结果
'''
    ['_Student__age', '_Student__pr2', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_name', '_pr', 'gender']
这里就解释了上面 “调用私有的实例属性和方法” 的写法
 '''












