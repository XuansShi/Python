#示例6-1：字符串的相关处理方法1
#一、大小写转换
    #（一）转小写
s1= "HELLOWORLD"
new_s2=s1.lower()
print(new_s2)
    #（二）转大写
s2 = "hello world"
new_s3=s2.upper()
print(new_s3)

#二、字符串的分割
s3 = "z3356782747@163.com"
lst = s3.split("@")#以@进行分割，得到列表,lst[0]是z3356782747 lst[1]是163.com
print("邮箱名：",lst[0],"域名：",lst[1])



#三、统计子串在字符串中的出现次数
s4 = "looooooooooser~~~~~~~"
print("o的出现次数为：",s4.count("o"))


#四、字符串的检索操作
s5="qwertyuiop"
print(s5.count("a"))#a在s5中的出现次数为0
print(s5.find("o"))#打印o首次出现的索引
print(s5.find("a")) #"a"不是s5的子串，所以返回-1
#print(s5.index("a"))# index与find效果相似，但index()找不到目标时程序报错


#五、判断开头结尾
s6 = "asdfghjkl"
print(s6.startswith("a")) # 查询是否以子串"a"开头
print(s6.startswith("m")) # 查询是否以子串"m"开头

print(s6.endswith("l")) # 查询是否以子串"l"结尾
print(s6.endswith("n")) # 查询是否以子串"n"结尾


