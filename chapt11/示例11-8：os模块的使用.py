# 示例11-8：os模块的使用
import os

# 1 获取当前的工作路径
print("当前工作路径",os.getcwd())

# 2 获取路径下的文件和目录信息
lst=os.listdir()
print("当前路径下的所有目录及文件",lst)
print("指定路径下所有的目录及文件",os.listdir("D:/xxzl"))


# 3 创建目录
# os.mkdir("hhh")  # 如果存在同名文件夹则程序报错
    # 创建多级目录
# os.mkdir("./aa/bb/cc")



# 4 删除目录
# os.rmdir("hhh")
    # 删除子目录及其父目录
# os.rmdir("./aa/bb/cc")



# 5 改变当前的工作路径
os.chdir("D:/xxzl")
print("当前工作路径",os.getcwd())



# 6 遍历目录树
for dirs,dirlst,filelst in os.walk("D:/xxzl"):
    print(dirs)
    print(dirlst)
    print(filelst)
    print("---------------------")







