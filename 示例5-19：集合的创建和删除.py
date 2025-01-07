#示例5-19：集合的创建和删除
  #一、集合的创建
    #(一)使用大括号{}创建
s ={10,20,30} #如果你直接写一个 s={} 创建得到的是字典而不是集合
print(s)
  #集合本身是可变数据类型，但只能存储不可变数据类型：
  #s1 = {[10,20]}#以列表为例
  #print (s1)#会报错：TypeError: unhashable type: 'list' 列表是没有哈希的数据类型


s3 = {"hello"}
print(s3)#打印得到无序的 h e l o,证明集合内部是无序且不重复的




    #(二)使用函数set创建
s2 = set()#使用set创建一个空集合
print(s2,type(s2))
    #可以用 列表 + set 创建集合：
s4 = set([1,2,3,4,5,6,7,8,9])
print(s4)
    #可以用 range + set 创建集合：
s5 = set(range(1,11))
print(s5)

    #二、列表的相关操作-集合
print('max:',max(s5))
print('min:',min(s5))
print('len:',len(s5))

print('9在集合中存在吗？',(9 in s5))
print('9在集合中不存在吗？',(9 not in s5))


    #三。集合的删除
del s5



























