#示例6-4：format的格式控制

'''
链接6-3：

# 三、format方法
print('姓名:{0},年龄:{1},成绩:{2}'.format(name,age,score))
print('姓名:{2},年龄:{0},成绩:{1}'.format(age,score,name))
    #模板字符串{}里的序号对应的是format()小括号里的序号

'''


s='helloworld'
# 一、引导符、填充、对齐方式-示例
        # 引导符号以及众符号 写在{}内数字的右侧
print('{0:*<20}'.format(s)) #左对齐，字符串的显示宽度为20，空白部分使用  * 号填充
print('{0:*>20}'.format(s)) #右对齐
print('{0:*^20}'.format(s)) #居中对齐 ^

print(s.center(20,'*'))# 居中对齐 center


# 二、千位分隔符（只适用于整数和浮点数）
print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.7865))
        #三位一逗号

# 三、浮点数小数部分的精度
print('{0:.2f}'.format(3.1419826))
# 字符串类型 .表示是最大的显示长度
print('{0:.5}'.format('helloworld')) #最大的显示长度是5，所以显示hello


# 四、类型
    #（一）整数类型
a=425
print('二进制:{0:b},十进制:{0:d},八进制:{0:o},十六进制:{0:x},十六进制：{0:X}'.format(a))#只需要写一个format

    #（二）浮点数类型
b=3.1415926
print('保留两位小数{0:.2f},科学计数法{0:.2E},科学计数法{0:.2e},百分数形式{0:.2%}'.format(b) )


