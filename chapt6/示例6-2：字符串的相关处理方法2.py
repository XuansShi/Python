#示例6-2：字符串的相关处理方法2
s1='HelloWorld'

# 一、字符串的替换
new_s=s1.replace('o','你好',1) # 最后一个参数是替换次数，默认是全部替换
print(new_s)

# 二、字符串在指定的宽度范围内居中，使用fillchar填充
print(s1.center(20))
print(s1.center(20,'*'))#让 s1 在20个字符的宽度范围内居中对齐，剩余位置由*填充

# 三、str.center(width,fillchar)
    #（一）掉字符串左右的字符串（此处以空格为例）
s2='    Hello    World    '
print(s2.strip()) #
print(s2.rstrip()) # 去除字符串右侧的空格
print(s2.lstrip()) # 去除字符串左侧的空格


    #（二）去掉指定的字符
s3='dl-Helloworld'
print(s3.strip('ld')) # 删除掉的字符与你传入的顺序无关
print(s3.lstrip('ld'))
print(s3.rstrip('dl'))

# 四、str.join(iter)
s4="666"
iter = ["A","B","C"]
iter666 = s4.join(iter)#在iter的每个元素的后面都加一个新字符串666,
for i in iter666:
    print(i," ")


#易错：这些操作大都没有修改实参
