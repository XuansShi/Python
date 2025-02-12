#示例6-10：search函数的使用
import re # 导入
pattern='\d\.\d+' # 模式字符串

s='I study Python3.11 every day Python2.7 I love you' # 待匹配字符串
match=re.search(pattern,s) # 匹配第一个符合的值
print(match) # 打印search结果
print(match.group()) # 返回与匹配到的子字符串


s2='4.10 Python I study every day'
match2=re.search(pattern,s2)
print(match2)
print(match2.group())

s3='I study Python every day'
match3=re.search(pattern,s3) # 没有符合的对象，返回None
print(match3)
