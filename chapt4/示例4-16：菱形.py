#示例4-16：菱形
row=eval(input('请输入菱形的行数:'))
while row%2==0: # 判断行数的奇偶性，行数是偶数，重新输入行数
    print('重新输入菱形的行数:')
    row=eval(input('请输入菱形的行数:'))

#菱形的上半部分的行数
top_row=(row+1)//2

#打印上半部分：
for i in range(1,top_row+1): #
    for j in range(1,top_row+1-i):
        print(' ',end='')
    for k in range(1,i*2):# 1,3,5,7...等腰三角形 range(1,2) ,range(1,4),range(1,6),  range(1,8),,,range(1,10)
        print('*',end='')
    print() # 当两个并列的for循环执行完毕之后，再换行
'''
&&&&*
&&&***
&&*****
&*******
*********
&*******
&&*****
&&&***
&&&&*
'''

# 下半部分
bottom_row=row//2
for i in range(1,bottom_row+1):
    #由空格组成的直角三角形
    for j in range(1,i+1):
        print(' ',end='')
    # 倒三角
    for k in range(1,2*bottom_row-2*i+2): # 1 -->range(1,8) ,2-->range(1,6) ,3-->range(1,4) ,range(1,2)
        print('*',end='')
    print()





