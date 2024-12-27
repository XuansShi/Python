#示例3-6：浮点数类型的使用
height = 187.6
print(height)#打印height
print(type(height))#查看height的数据类型

a = 18
print(a)
print(type(a))#int类型

b=18.0
print(b)
print(type(b))#float类型
#虽然在数值上a b 大小一致，但是数据类型不同



#科学计数法
x=1.99e5  #e前后必须要有数字，e前是系数，e后是10的指数，指数只能为整数
print("使用科学计数法表示1.99e5",x,"x的数据类型是",type(x))




#两个浮点型运算后，有概率得到不确定的尾数 问题
print(0.1+0.2)
#你可以用round函数来保留n位小数
print("用round函数来保留n位小数",round(0.1+0.2,1))