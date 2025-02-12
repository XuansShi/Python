# 第9章-实战题三：使用面向对象思想实现乐器弹奏：
# 创建乐器父类
class Instrument():
    def make_sound(self):
        pass

# 创建乐器子类
class Erhu(Instrument):
    def make_sound(self):# 子类重写父类方法
        print("二胡在弹奏")

class Pinao(Instrument):
    def make_sound(self):
        print("钢琴在弹奏")

class Violin(Instrument):
    def make_sound(self):
        print("小提琴在弹奏")

# 编写一个函数
def play(obj):# 传入一个对象
    obj.make_sound()


# 实例化
er=Erhu()
pin=Pinao()
vi=Violin()

# 调用make_sound方法
play(er)
play(pin)
play(vi)











