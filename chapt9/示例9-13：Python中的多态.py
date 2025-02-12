# 示例9-13：Python中的多态
class Person(object):
    def eat(self):
        print("人次五谷杂粮")
    # 注：没有实例属性可以不写初始化方法。有实例属性应该在初始化方法里赋值，就像c++的构造函数一样

class Cat():
    def eat(self):
        print("猫猫喜欢吃鱼")

class Dog():
    def eat(self):
        print("狗子喜欢啃骨头")

# 以上三个类都有一个同名方法eat

# 实例化
per=Person()
cat=Cat()
dog=Dog()



# 编写函数
def fun(obj):# obj是函数的形参，此时不知道数据类型，程序运行的时候才知道。     与c++不同，c++会将所有的数据类型指明
    obj.eat() # 通过变量obj(对象)点出调用eat方法

# 调用fun函数
fun(per)
fun(cat)
fun(dog)
    # 动态决定调用哪个对象中的方法