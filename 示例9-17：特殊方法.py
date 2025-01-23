# 示例9-17：特殊方法
a = 10
b = 20
print(dir(a)) # 由于Python中一起皆对象，可以打印输出a的方法

# 执行加法运算
print(a+b) # 自动调用特殊方法
print(a.__add__(b)) #手动调用特殊方法















