#示例5-15：字典的创建和删除

#—————————————————————————————————————————————————————————————————————————————————————————
#字典的创建
#一、使用{}创建字典
d={10:'cat',20:'dog',30:'pet',20:'zoo'}
print(d) # key相同时，value值进行了覆盖


#二、使用内置函数dict创建字典
# (1)zip函数
lst1=[10,20,30,40]
lst2=['cat','dog','pet','zoo','car']
zipobj=zip(lst1,lst2)
print(zipobj) # <zip object at 0x000001ECD5A24F00>映射的结果是一个zip类型的对象

#print(list(zipobj)) # [(10, 'cat'), (20, 'dog'), (30, 'pet'), (40, 'zoo')]  可以通过list()将zip类型的对象转换为list列表类型的对象

d=dict(zipobj) #讲zip类型转换为字典类型
print(d) #打印结果为： {10: 'cat', 20: 'dog', 30: 'pet', 40: 'zoo'}

# (2)使用参数创建字典
d=dict(cat=10,dog=20) # 等号左侧的是key ,右侧的是value
print(d)

#—————————————————————————————————————————————————————————————————————————————————————————
#复合字典
#1.可以使用元组作为字典的key
t=(10,20,30)
print({t:10}) # t是key,10是value ,元组是可以作为字典中的key

#2.不能使用列表作为字典的key
# lst=[10,20,30]
# print({lst:10}) # TypeError: unhashable type: 'list'
# 可变数据类型不能作为字典的键

#————————————————————————————————————————————————————————————————————————————————————————————
# 序列的相关操作-字典
print('max:',max(d))# 字典的最大值
print('min:',min(d))# 字典的最小值
print('len:',len(d))# 字典的长度
del d# 字典的删除

#print(d)  #都删了自然无法打印了

