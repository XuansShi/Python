#示例3-14：eval函数的使用
  #去掉对象最外层的引号(然后执行去掉引号后的语句)
s="3.14+3"
print("s的值：",s,"s的数据类型：",type(s))
print("利用eval函数执行s的引号内的语句：",eval(s))# 去掉引号后执行了 3.14+3 加法运算  得到6.14000000001

#eval函数经常和input函数联动，用来获取用户输入的数值：
age = eval(input("请输入您的年龄"))  #习：input函数的输入值都会变成字符串类型   此处和eval一起使用就相当于执行了int(age)操作
print("age的数值 =",age,"age的类型：",type(age))#下同

height = eval(input("请输入您的身高"))  #相当于在输入后执行了float(height)操作，再赋值给height   注：一般认为身高是float类型
print("height的数值 =",height,"height的类型：",type(height))