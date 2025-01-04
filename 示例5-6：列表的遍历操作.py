#示例5-6：列表的遍历操作
lst=['hello','world','python','php']
# 一、使用遍历循环for遍历列表元素
for item in lst:
    print(item)

# 二、使用for循环,range()函数，len()函数，根据索引进行遍历
for i in range(0,len(lst)):
    print(i,'-->',lst[i])

# 三、使用enumearte()函数便利
for index,item in enumerate(lst):
    print(index,item) #index是序号，不是索引

# 手动修改序号的起始值（不修改则默认为0）
for index,item in enumerate(lst,start=1):
    print(index,item)

for index, item in enumerate(lst,1):  #  省略start不写，直接写起始值
    print(index, item)
