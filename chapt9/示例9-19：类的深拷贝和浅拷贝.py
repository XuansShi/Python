# 示例9-19：类的深拷贝和浅拷贝
class CPU():
    pass
class Disk():
    pass

class Computer():
    def __init__(self,cpu,disk):
        self.cpu=cpu
        self.disk=disk


cpu=CPU()
disk=Disk()

# 创建一个计算机对象
com =Computer(cpu,disk)

# 对象的赋值
com1 =com
print(com,"字对象的内存地址：",com.cpu,com.disk)
print(com1,"字对象的内存地址：",com1.cpu,com1.disk) # com1 和 com 打印的地址完全一致

# 类对象的浅拷贝
import  copy
com2 = copy.copy(com) #com2是新产生的对象，但其子对象还是cpu和disk
print(com2,"字对象的内存地址：",com2.cpu,com2.disk) #com2的内存地址相较于com1发生了改变，但子对象的不变



# 类对象的深拷贝
com3 = copy.deepcopy(com)
print(com3,"字对象的内存地址：",com3.cpu,com3.disk) #com3是新产生的对象，虽然其子对象是cpu和disk，但是三者的地址都发生了改变





































