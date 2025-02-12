#示例4-12：无限循环扩展 while else

#语法：如果在语句块中没有break，则循环正常结束后，接着执行else语句块
'''
初始化变量
while 条件:
    语句块
    修改变量
else:
    语句块
'''

sum = 0
i = 0
while i<101:
    sum = sum + i
    i+=1
else:
    print(sum)













