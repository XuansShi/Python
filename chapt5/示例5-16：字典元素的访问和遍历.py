#示例5-16：字典元素的访问和遍历
d={'hello':10,'world':20,'python':30}#习：字符串是不可变序列，所以字符串可以作键

#——————————————————————————————————————————————————————————————————
# 访问字典中的元素
# (1)使用d[key]
print(d['hello'])
#(2)d.get(key)
print(d.get('hello'))

# 两种方法的区别：
  # 如果key不存在，d[key]会报错,但d.get(key)可以指定默认值：
   # 1.  d[key]
#print(d['java']) # 报错KeyError: 'java'

   # 2.  d.get(key)
print(d.get('java')) # None
print(d.get('java','不存在'))


#——————————————————————————————————————————————————————————————————
# 字典的遍历
# 仅获取item
for item in d.items():
    print(item) # key=value组成的一个元素

# 分别获取key,value
for key,value in d.items():
    print(key,'--->',value)
