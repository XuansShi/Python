# 第8章-实战题二：提取字符串中所有的数字并求和

# 函数实现
def get_digit(x):
    s = 0 #存储累加和
    lst = [] #存储提取出来的数字
    for item in x:
        if item.isdigit(): #如果提取出来的是数字
            lst.append(int(item)) # 将提取出来的数字插入到预备的容器末尾
    # 使用内置函数sum求和
    s = sum(lst)
    return lst,s #返回 列表 和 累加和

# 函数调用
s = input("请输入一个字符串")
lst,x=get_digit(s)
print("提取出的数字列表为",lst)
print("累加和为",x)














