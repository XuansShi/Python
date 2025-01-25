# 第9章-实战题四：使用面向对象思想编写出租车和家用轿车类
class Car():
    def __init__(self,type,no):
        self.type = type
        self.no = no

    def start(self):
        print("我是车，我能启动")
    def stop(self):
        print("我是车，我能停止")


# 创建子类
class Taxi(Car):
    def __init__(self,type,no,conpany):
        super().__init__(type,no) #调用父类的方法进行初始化
        self.conpany = conpany

    # 重写父类的启动和停止方法
    def start(self):
        print("乘客您好！")
        print(f"我是{self.conpany}公司，我的车牌号是：{self.no},您要去哪里？")

    def stop(self):
        print("目的地到了，欢迎下次乘坐")


class FamilyCar(Car):
    def __init__(self,type,no,name):
        super().__init__(type,no)
        self.name = name

    def start(self):
        print(f"这是{self.name}的轿车")

    def stop(self):
        print("目的地到了，肘！")



# 实例化
taxi= Taxi("雷神工业","沪A66666","终末地工业")
taxi.start()
taxi.stop()

familycar= FamilyCar("逆熵","京A88888","瓦大爷")
familycar.start()
familycar.stop()










