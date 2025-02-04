# 第11章-实战题一：批量创建文件
import random
import os
import os.path

# 创建文件名的函数
def create_filename():
    filename_lst=[]
    lst=['水果','蔬菜','肉蛋']
    code=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    for i in range(1,11):
        filename=''
        if i<10:
            filename+='0'+str(i)
        else:
            filename+=str(i)
        # 拼接类别
        filename+="_"+random.choice(lst) #从列表中随机选择一个
        # 拼接识别码
        s=''
        for j in range(9):
            s+=random.choice(code)
        filename+='_'+s
        filename_lst.append(filename)
    return filename_lst

# 创建文件的函数
def create_file(filename):
    with open(filename,'w') as file:
        pass




if __name__ == '__main__':
    # 在指定路径创建文件
    path='./data'
    if not os.path.exists(path):
        os.mkdir(path)

    lst=create_filename()
    for item in lst:
        create_file(os.path.join(path,item)+'.txt')













