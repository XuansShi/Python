#示例4-4：多分支结构的使用
score=eval(input('请输入您的成绩:'))
# 多分支结构
if score<0 or score>100:
    print('成绩有误！')
elif 0<=score<60:#注意c/c++不能写成这种有两个端点的形式
    print('E')
elif 60<=score<70:
    print('D')
elif 70<=score<80:
    print('C')
elif 80<=score<90:
    print('B')
else:
    print('A')