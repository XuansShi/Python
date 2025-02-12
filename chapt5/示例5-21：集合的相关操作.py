#示例5-21：集合的相关操作
s={10,20,30}
# 一、集合的增删操作：
# 1.使用s.add()向集合中添加元素
s.add(100)
print(s)

# 2.使用s.remove()删除元素
s.remove(20)
print(s)

# 3.使用s.clear()清空集合中所有元素
# s.clear()
# print(s)


# 二、集合的遍历操作
    # 1.使用for
for item in s:
    print(item)

    # 2.使用enumerate()函数
for index,item in enumerate(s):
    print(index,'-->',item)

# 三、集合的生成式
s={i for i in range(1,10)}
print(s)
    #生成式+if
s={i for i in range(1,10) if i%2==1}
print(s)
