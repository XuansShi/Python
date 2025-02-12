#示例5-17：字典操作的相关方法
d={1001:'李梅',1002:'王华',1003:'张峰'}
print(d)

# 1.向字典中添加元素
d[1004]='张丽丽'  # 直接使用赋值运算符向字典中添加元素
print(d)

# 2.获取字典中所有的key
keys=d.keys()
print(keys) # dict_keys([1001, 1002, 1003, 1004])  打印出的是一个dict_keys类型的数据
print(list(keys))# 转换为列表
print(tuple(keys))# 转换为元组

# 3.获取字典中所有的value
values=d.values()
print(values) # dict_values(['李梅', '王华', '张峰', '张丽丽'])
print(list(values))
print(tuple(values))

# 4.先将字典中的item转成key-value的形式,再以元组的方式进行展现：
lst=list(d.items())
print(lst)

d=dict(lst)
print(d)

# 5.pop函数
print(d.pop(1001))
print(d)

print(d.pop(1008,'不存在'))#已知1008时的键值对不存在，你可以这样写然后在打印的时候会返回“不存在


# 6.popitem随机删除
print(d.popitem())
print(d)


# 7.清空字典中所有的元素
d.clear()
print(d)
# Python中一切皆对象，而且每个对象都有一个布尔值
print(bool(d)) # 空字典的布尔值为False





































