# 第8章-实战题三：字符串中字母大小写转换
# 函数实现
def lower_upper(x):
    lst = []
    for item in x:
        if 'A'<=item<='Z':#如果在这个范围内那就是大写字母
            lst.append(chr(ord(item)+32)) # 先用ord函数转为unicode码，再用chr函数把unicode码转为对应的字符串，然后插入列表lst的末尾
        if 'a'<=item<='z':#如果在这个范围内那就是小写字母
            lst.append(chr(ord(item)-32))
        else:lst.append(item)#如果既不是大写字母也不是小写字母就直接添加进来

    return ''.join(lst) #拼接列表的所有元素为一个字符串，然后返回

# 函数调用
s = input("请输入一个字符串")
new_s = lower_upper(s)
print(new_s)










