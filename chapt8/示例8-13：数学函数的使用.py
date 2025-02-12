# 示例8-13：数学函数的使用
print('绝对值:',abs(100),abs(-100),abs(0))
print('商和余数:',divmod(13,4))
print('最大值:',max('hello'))
print('最大值:',max([10,4,56,78,4]))
print('最小值:',min('hello'))
print('最小值:',min([10,4,56,78,4]))

print('求和:',sum([10,34,45]))
print('x的y次幂:',pow(2,3))

# 四舍五入
print(round(3.1415926)) # round函数只有一个参数时，保留整数
print(round(3.9415926)) # 四舍五入，结果为4
print(round(3.1415926,2)) # 保留2位小数
print(round(314.15926,-1)) # 结果为314；保留-1位小数：个位进行四舍五入
print(round(314.15926,-2)) # 结果为300；保留-2位小数：十位进行四舍五入











