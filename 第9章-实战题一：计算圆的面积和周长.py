# 第9章-实战题一：计算圆的面积和周长
class Circle:
    def __init__(self,radius):
        self.radius=radius

    # 计算面积的方法
    def get_area(self):
        return 3.14*pow(self.radius,2)

    # 计算周长的方法
    def get_perimeter(self):
        return 2*self.radius*3.14


# 实例化
r = eval(input("请输入圆的半径"))
c=Circle(r)

# 调用方法
area=c.get_area()
per=c.get_perimeter()
print("圆的面积 =  ",area)
print("圆的周长 = ",per)











