# 示例8-11：斐波那契数列
# 函数实现：
def fac(n):
    if n==1 or n==2:
        return 1
    else:
       return  fac(n-1)+fac(n-2)

# 打印斐波那契数列第9位上的数字
print(fac(9))

#打印前9位的数字
for i in range(1,10):
    print(fac(i),end='\t')






