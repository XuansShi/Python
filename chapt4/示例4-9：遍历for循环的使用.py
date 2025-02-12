#示例4-9：遍历for循环的使用

#一、遍历字符串：
for i in "HELLOWROLD":
    print(i)


#二、遍历数组
for i in range(1,11):#从[1,11)左闭右开区间取出整数
    if i%2 == 0:#如果是偶数就输出
        print(i)

#计算1~10的整数的累加和
sum = 0
for j in range(1,11):
    sum = sum + j
    print(sum)

#100~999间的水仙花数
for i in range(100,1000):
    gw = i%10
    sw = (i//10)%10
    bw = i//100
    if gw**3+sw**3+bw**3==i:
        print(i,"是水仙花数")




















