#示例4-3：双分支结构if-else
number=eval(input('请输入您的6位中奖号码:'))
# if...else
if number==987654:
    print('恭喜您中奖了！')
else:
    print('您未中本期大奖！')



print('----以上代码可以使用条件表达式进行简化---')#因为上面的双分支if的语句块中都只有一句话，所以可以写成下面的形式：
result = "恭喜中奖！"if number == 987654 else "谢谢参与"
print(result)

#当然也可以跳过赋值直接输出：
print('恭喜您中奖了!' if number==987654 else '您未中本期大奖!')