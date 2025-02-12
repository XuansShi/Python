#示例6-9：match函数的使用
# 导入re模块
import re

# 先用正则表达式写一个匹配的规则（模式字符串）
pattern='\d\.\d+' # \d 匹配十进制数    \. 将.作为普通字符使用     + 限定符，匹配前面的字符一次或多次  ： 找到类似于3.11的数字

# 待匹配字符串一
s='I study Python 3.11 every day'
# 匹配
match=re.match(pattern,s,re.I) # re.I就是ignore忽略大小写
             # 发现python允许变量和成员函数同名
# 打印
print(match) # None 因为match是从头开始查找的，但是s的开头不是数字


# 待匹配字符串二
s2='3.11Python I study every day'
match2=re.match(pattern,s2)
print(match2) # <re.Match object; span=(0, 4), match='3.11'>

print('匹配值的起始位置:',match2.start())
print('匹配值的结束位置:',match2.end())
print('匹配区间的位置元素:',match2.span()) # span返回匹配的位置区间
print('待匹配的字符串:',match2.string)
print('匹配的数据:',match2.group()) # group返回与模式匹配的子字符串


















