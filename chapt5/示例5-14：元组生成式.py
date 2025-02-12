#示例5-14：元组生成式
t=(i for i in range(1,4))
print(t)#这样打印得到的是生成器对象


#类型转换为元组
t = tuple(t)
print(t)
#遍历
for i in t:
    print(i)
   #注意遍历一遍后该对象里就不存在元素了（类似于getchar）
                              


#使用__next__方法遍历生成器对象
t1=(i for i in range(1,5))
print(t1.__next__())#这样一次只能取出一个元素
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())#把生成器对象全取出来后t1里就没有东西了
t1=tuple(t1)
print(t1)#此时再转换并且打印会得到空的t1






















