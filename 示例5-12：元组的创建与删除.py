#示例5-12元组的创建与删除

#元组的创建
# 一、使用小括号创建元组
t=('hello',[10,20,30],'python','world')
print(t)

# 二、使用内置函数tuple()创建元组
t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)



#序列的相关操作-在元组的应用
print('10在元组中是否存在：',(10 in t))
print('10在元组是不存在:',(10 not in t))
print('最大值:',max(t))
print('最小值:',min(t))
print('len:',len(t))
print('t.index:',t.index(10))
print('t.count',t.count(10))


#元组的删除
del t
#print(t) #报错





# 如果元组中只有一个元素，逗号不能省
y=(10,)
print(y,type(y))#数据类型为元组

#如果元组中只有一个元素，而且你省略了逗号：
t=(10)
print(t,type(t))#这里会打印数据类型为int



