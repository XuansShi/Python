#示例3-18：逻辑运算符的使用

"""
and：只要有一假则为假
or：只要有一真则为真
not：逻辑取反


注意：
逻辑与、逻辑或   从左到右  计算
逻辑非   从右到左 计算，先运行等号右边的表达式，再对结果取反
"""

#C++用的是符号，Python可以用英文

print(True and True)#True

print(False and 10/0) #False  只要and左侧的表达式结果为False，右边的表达式就不会运行了，直接返回False

print(True or 10/0) #Ture 只要or左侧的表达式结果为True，右侧的表达式就不会运行了，直接返回True

