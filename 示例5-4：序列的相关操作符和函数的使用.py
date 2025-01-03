#示例5-4：序列的相关操作符和函数的使用
s='helloworld'

# in的使用
print('e在helloworld中存在吗?',('e'in s))
print('v在helloworld中存在吗?',('v'in s))


# not in 的使用
print('e在helloworld中不存在吗?',('e'not in s))
print('v在helloworld中不存在吗?',('v'not in s))


# 内置函数的使用
print('len():',len(s))#len 求序列长度

print('max():',max(s))#max 求序列的最大值

print('min():',min(s))#min 求序列的最小值



# 序列对象的方法，使用序列的名称，打点调用
  #index ：
print('s.index():',s.index('o')) #o在s中第一次出现的索引位置 4
#print('s.index():',s.index('v')) #报错：ValueError: substring not found ,报错的原因是v在字符串中根本不存在，不存在所以找不到

  #count ：
print('s.count():',s.count('o')) #统计o在字符串s中出现的次数












