# 第11章-实战题二：批量创建目录
import os
import os.path

def mkdirs(path,num):
    for item in range(num):
        os.mkdir(path+'/'+str(item))

if __name__ == '__main__':
    path='./newdir'
    if not os.path.exists(path):
        os.mkdir(path)

    num = eval(input("请输入需要创建目录的个数"))
    mkdirs(path,num)













