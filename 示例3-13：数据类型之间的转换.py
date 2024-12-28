#一、隐式转换
print("——————隐式转换——————")
x=10
y=3
z=x/y
print(z,type(z))  #通过运算，将两个整数的运算结果转换为float类型(因此是隐式转换)


#二、显式转换：
print("——————显式转换——————")
#float转int
print("float转int ———— 3.14  ：",int(3.14))
print("float转int ———— -3.14  ：",int(-3.14))

print(int(z),type(z))  #发现这样输出 虽然结果的小数部分都没了，但是z依然是float类型。也就是说int函数不会修改实参
#像这样才是修改了z的类型：
zz=int(z)
print(int(zz),type(zz))



#int转float
#就是在整数后面加上一位小数  如10变为10.0



#str转int
print(int("100")+int("100"))

  #字符串转int可能会报错的情况：
  #1 字符串不是十进制数   比如说18a
  #2 字符串不是整数      比如说3.14



#chr()函数  和   ord()函数
  #chr()函数： 将unicode码转为字符
  #ord()函数： 将字符转为unicode码



#进制之间的转换操作
  #注意转换后的结果是字符串类型
print("——————进制之间的转换操作——————")
print("十进制转十六进制",hex(86))
print("十进制转八进制",oct(86))
print("十进制转二进制",bin(86))






