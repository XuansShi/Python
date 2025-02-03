# 示例11-7：高维数据的存储
import json
# 准备高维数据
lst = [
    {'name':"xs","age":18,"score":99}

]

s=json.dumps(lst,ensure_ascii=False,indent=4) # ensure_ascii正常显示中文,indent增加数据的缩进（好看用

print(type(s),s) # 编码list-->str，列表中是字典

# 解码
lst2=json.loads(s)
print(type(lst2),lst2)


# 编码到文件中
with open("student.txt",'w')as file:
    json.dump(lst,file,ensure_ascii=False,indent=4)

# 解码到程序
with open("student.txt",'r')as file:
    lst3=json.load(file)
    print(type(lst3),lst3)


