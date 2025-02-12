num = input("请输入您的幸运数字")
print("您的幸运数字为"+num)#运行正常，说明此时的num是字符串类型

num = int(num)#使用内置函数int将num转换成int类型
print("您的幸运数字是",num)