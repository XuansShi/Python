#示例5-8：列表的排序操作
    #sort函数原型：
     #ist.sort(key=None.reverse=False)
     
lst=[4,56,3,78,40,56,89]
print('原列表:',lst)

# 排序，默认升序
lst.sort() # 排序是在原列表的基础上进行的，不会产生新的列表对象
print('升序:',lst)

#排序，降序
lst.sort(reverse=True)
print('降序:',lst)


print('-----------------------------')


lst2=['banana','apple','Cat','Orange']

print('原列表：',lst2)
# 升序排序，先排大写，再排小写（大写字母的ASCII码比对应的小写字母小32）
lst2.sort()
print('升序:',lst2)

# 降序，先排小写，后排大写
lst2.sort(reverse=True)
print('降序:',lst2)

# 忽略大小写进行比较
lst2.sort(key=str.lower)#str.lower代表把所有的字符串都转换为小写#注意参数不需要加括号
print(lst2)

