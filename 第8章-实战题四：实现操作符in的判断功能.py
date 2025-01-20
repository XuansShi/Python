# 第8章-实战题四：实现操作符in的判断功能
# 函数实现
def get_find(s,lst): #传入两个参数，一个是要查找的字符，一个是被查找的字符串
    for item in lst:
        if s == item:
            return True # 找到了直接返回True，函数结束
    return False # 到这一步时，整个循环全部结束，代表没有找到需要查找的字符串，所以返回False

# 函数调用
lst = ['hello','world','python','kiana']
s = input("请输入要判断的字符串：")
result = get_find(s,lst)
print("存在"if result else  "不存在")# 输出判断结果；     此处使用三目运算符（条件表达式）实现对应功能







