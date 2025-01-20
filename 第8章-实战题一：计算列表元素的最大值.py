# 第8章-实战题一：计算列表元素的最大值
# 创建列表
import  random #包含生成随机数函数的模块
lst = [random.randint(1,100) for item in range(10)]# 使用列表生成式生成10个1到100之间的随机数

# 函数实现
def get_max(lst):
    x = lst[0] #用x存储元素的最大值
    #遍历
    for i in range(1, len(lst)):
        if lst[i]>x:
            x = lst[i]#如果你遍历到的元素比当前已知的最大值大，那么它就是最大值
    return x

# 调用
print("lst中的最大值为",get_max(lst))