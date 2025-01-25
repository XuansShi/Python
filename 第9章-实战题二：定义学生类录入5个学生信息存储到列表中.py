# 第9章-实战题二：定义学生类录入5个学生信息存储到列表中
class Student(object):
    def __init__(self, name, age,gender,score):
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    # 用于输出信息的实例方法
    def info(self):
        print(self.name, self.age, self.gender, self.score)

print("请输入5位学生的信息，格式为 姓名#年龄#性别#成绩")
lst=[]
for i in range(1,6):
    s= input(f'请输入第{i}位学生信息以及成绩')
    s_lst=s.split('#') # 字符串的分割方法-以#井号分割；索引为0 1 2 3 分别对应 姓名 年龄 性别 成绩

    # 创建学生对象
    stu=Student(s_lst[0],s_lst[1],s_lst[2],s_lst[3])

    # 将学生对象添加到列表中
    lst.append(stu)

# 遍历列表，调用学生的info方法
for item in lst:
    item.info()









