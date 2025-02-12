#示例4-17：空心菱形
  #由于只打印每行首尾的*，所以只需要在示例4-16的基础上，加上判断即可
num = eval(input("请输入菱形的总行数"))
while num%2==0:
    print("输入错误请输入奇数")
    num=eval(input("请重新输入菱形的总行数"))

top_num=(num+1)//2
# 上半部分
for i in range(1,top_num+1):
    for j in range(1,top_num+1-i):
        print(" ",end="")
    for k in range(1,i*2):
        if k==1 or k==i*2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

#下半部分
for i in range(1,top_num):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1, (top_num-i)*2+1):
        if k==1 or k==(top_num-i)*2-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()