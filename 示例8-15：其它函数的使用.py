# 示例8-15：其它函数的使用
# format(value,format_spec) 将value以format_spec格式进行显示
print(format(3.14,'20')) # 数值型默认右对齐
print(format('hello','20')) # 字符串默认左对齐
print(format('hello','*<20')) # <左对齐，*表示的填充符，20表示的是显示的宽度
print(format('hello','*>20')) # >右对齐
print(format('hello','*^20')) # ^居中对齐


print(format(3.1415926,'.2f')) # 3.14
print(format(20,'b'))
print(format(20,'o'))
print(format(20,'x'))
print(format(20,'X'))
print('-'*40)

# len() 获取对象的长度或者元素个数
print(len('helloworld'))
print(len([10,20,30,40,50]))
print('-'*40)

# id() 获取对象内存地址
print(id(10))
print(id('helloworld'))

# type() 获取对象数据类型
print(type('hello'),type(10))

# eval(s) 执字符串s所表示的Python代码（去掉字符串左右的引号）
print(eval('10+30'))
print(eval('10>30'))











