# 示例6-11：findall函数的使用
import re # 导入
pattern='\d\.\d+' # +限定符，\d 0-9数字出现1次或多次

s='I study Python3.11 every day Python2.7 I love you'
lst=re.findall(pattern,s)
print(lst) # ['3.11', '2.7']

s2='4.10 Python I study every day'
lst2=re.findall(pattern,s2)
print(lst2) # ['4.10']

s3='I study Python every day'
lst3=re.findall(pattern,s3)
print(lst3) # 没有符合的结果，打印空列表
