# 示例8-6：函数的返回值的使用
# 函数的返回值

# 一、无返回值的函数
def calc(a,b):
    print(a+b)

calc(10,20)
print(calc(1,2)) #None

# 二、一个返回值的函数
def calc2(a,b):
    s=a+b
    return s  # 将s返回给函数的调用处去处理


get_s=calc2(1,2) # 存储到变量中
print(get_s)

get_s2=calc2(calc2(1,2),3)  # 1+2+3  先去执行calc2(1,2) 返回 结果为3，再去执行calc2(3,3)
print(get_s2)


# 三、多个返回值的函数
def get_sum(num):
    s=0# 累加和
    odd_sum=0 # 奇数和
    even_sum=0 # 偶数和
    for i in range(1,num+1):
        if i%2!=0: # 说明是奇数
            odd_sum+=i
        else:
            even_sum+=i
        s+=i
    return odd_sum,even_sum,s # 三个值




result=get_sum(10)
print('type(result) = ',type(result))
print('result = ',result)

# 解包赋值
a,b,c=get_sum(10) # 返回3个值，元组类型
print(a)
print(b)
print(c)













