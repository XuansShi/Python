#示例4-11：无限循环while
 #基本步骤：
  #第一步 初始化变量：
  #第二步 条件判断：
  #第三步 语句块：
  #第四步 改变变量：

#例子一：
  #第一步 初始化变量：
answer = input("今天要上课嘛？回答y  or  n  ")
  #第二步 条件判断：
while answer=="y":
  #第三步 语句块：
    print("好好学习天天向上")
  #第四步 改变遍历：
    answer = input("今天要上课嘛？回答y  or  n  ")


#例子二：
#在Python使用while实现类似于 for(i =0;i<101;i++){sum=sum+i;} ：
sum = 0
i = 0
while i<101:
    sum = sum + i
    i+=1#注意Python没有++/--













