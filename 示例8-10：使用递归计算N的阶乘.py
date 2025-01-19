# 示例8-10：使用递归计算N的阶乘
def fac(n):  #算法：n的阶乘  N!=N*(N-1)!.......1!=1
    if n == 1:  #分段函数不要漏写了
        return 1
    else:
        return n * fac(n - 1)  # 自己调用自己


print(fac(5))  # 5!=5*4*3*2*1  =120












