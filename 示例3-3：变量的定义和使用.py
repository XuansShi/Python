luck_number = 2 #创建一个整形变量luck_number ，且赋值为2

my_name ="禤莳" #创建字符串类型的变量my_name

print("luck_number的数据类型是：",type(luck_number))


#python可以通过给变量赋予不同数据类型的值，来动态修改变量的数据类型
luck_number = "2"
print("luck_number的数据类型是：",type(luck_number))


#python允许多个变量指向同一个值
num1 = num2 = num3 = 10  #也就是这种连等
print("Python允许多个变量指向同一个值（允许连等）",num1,num2,num3)

print("查看num1、num2、num3的地址：",id(num1),id(num2),id(num3))#使用内置id()函数查看变量地址








