#示例6-8：字符串的去重操作
s='helloworldhelloworldadfdfdeoodllffe'

# (1)字符串拼接及not in
new_s=''
for item in s:
    if item not in new_s:
        new_s+=item # 拼接操作
print(new_s) # 拼接结果去掉了所有重复的内容


# (2)字符串拼接+索引+not in
new_s2=''
for i in range(len(s)):
    if s[i]  not in new_s2:
        new_s2+=s[i]
print(new_s2)

# (3)集合去重+列表排序
new_s3=set(s)           # 用内置set函数创建集合，以此去重
lst=list(new_s3)        # 将new_s3转为列表类型
lst.sort(key=s.index)   # 由于集合去重时打乱了操作，这里使用列表的内置函数sort，安装原字符串s的index进行排序
print(''.join(lst))

