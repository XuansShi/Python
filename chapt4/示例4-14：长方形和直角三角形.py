#示例4-14：长方形和直角三角形
#长方形
i = 0
j = 0
for i in range(1,11):
    for j in range(1,6):
        print("*",end="")
    print() # 空的print语句，换行



print('-----------------')



for i in range(1,6): # 5行
    # *的个数与行相同,range(1,2),第二行，range(1,3)
    for j in range(1,i+1):
        print('*',end='')
    print() # 空的print语句，换行


#如果用while循环会有点麻烦，而且可能语法出错




