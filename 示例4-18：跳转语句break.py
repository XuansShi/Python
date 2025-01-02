#示例4-18：跳转语句break
s=0# 存储累加和

#(1)初始化变量
i=1
#(2)条件判断
while i<11:
#(3)语句块
    s+=i
    if s>20:
        print('累加和大于20的当前数是:',i)
        break
    # (4)改变变量
    i+=1




print('--------------------------')


#(1)初始化变量
i=0 # 统计登录的次数
#(2)条件判断
while i<3:
#(3)语句块
    user_name=input('请输入用户名:')
    pwd=input('请输入密码:')
    if user_name=='ysj' and pwd=='888888':
        print('系统正在登录，请稍后...')
        break
    else:
        if i<2:
            print('用户名或密码不正确,您还有',2-i,'次机会')
#(4)改变变量
    i+=1#这句和上面的if 、 else都是并行的关系

else: # while...else
    print('三次均输入错误！')

