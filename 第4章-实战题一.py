#第4章-实战题一：
#输入一个年份，判断是否为闰年
num = eval(input("请输入年份"))
if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    print(num,"年是闰年")
else:
    print(num,"年是平年")