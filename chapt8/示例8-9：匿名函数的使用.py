# 示例8-9：匿名函数的使用
# 非匿名函数
def calc(a,b):
    return a+b

print(calc(10,20))


# 匿名函数
s=lambda a,b:a+b # s表示就是一个匿名函数
print(type(s)) # <class 'function'>

    # 匿名函数的调用：
print(s(10,20))


print('-'*30)


# 示例1：取值
lst=[10,20,30,40,50]
    #  1 列表的正常取值操作
for i in range(len(lst)):
    print(lst[i])

    # 2 使用匿名函数对列表取值
for i in range(len(lst)):
    result=lambda x:x[i] # 根据索引取值 ; result是的类型是 函数类型function , x是形式参数
    print(result(lst)) # lst是实际参数


# 示例2：排序
student_scores=[
    {'name':'陈梅梅','score':98},
    {'name': '王一一', 'score': 95},
    {'name': '张天乐', 'score': 100},
    {'name': '白雪儿', 'score': 65}
]
    # 按成绩从大到小对列表进行排序
student_scores.sort(key=lambda x:x.get('score'),reverse=True) #习：此处的key是sort函数的排序规则  ; 这里的x是字典
print(student_scores)

