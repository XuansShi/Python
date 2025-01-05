#示例5-13：元组的访问与遍历
t=('python','hello','world')

#使用索引访问元组-元组的切片操作
print(t[0])
t2=t[0:3:2]#从第0位开始，到第三位结束（不包括第三位），步长为2
print(t2)

#元组的遍历
#一、利用for循环
for i in t:
    print(i)
#二、利用索引
for i in range(0,len(t)):
    print(i,t[i])
#三、利用enumerate函数
for index,item in enumerate(t):
    print(index,"----->",item)

