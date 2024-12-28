#示例3-12：bool类型的使用
x = True
print(x)
print(type(x))

print(x+10)    #True是1 False是0
print(False+10)

#每一个对象都有一个bool值，可以使用内置函数bool来测试对象的布尔值
print("测试一下各种对象的布尔值：")
#数值：
print("#数值：")
print(bool(18))#True
print(bool(0),bool(0.0))#False
#总结 非0的整数布尔值都为True；
    # 0 0.0 虚数0为False

#字符：
print("#字符：")
print(bool("北京欢迎你"))#True
print(bool(""))#False
#总结 所有非空字符串的布尔值都是True，空字符串的布尔值是False

#Flase 和 None 的布尔值都是False
print("#Flase 和 None 的布尔值都是False")
print(bool(False),bool(None))

#布尔值为False：
#False   None
#0   0.0   虚数0
#空序列（空字符串、空元组、空列表、空字典、空集合）
#自定义对象的实例，该对象的__bool__()方法、__len()__返回False

