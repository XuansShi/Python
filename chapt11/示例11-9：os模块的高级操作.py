# 示例11-9：os模块的高级操作
import os

# 1 删除文件
# os.remove("./a.txt") # 如果删除的文件不存在则报错

# 2 重命名
# os.rename("./aa.txt,"nwaa.txt")


# 转换时间格式
import time
def date_format(longtime):
    s=time.strftime('%Y-%m-%d #H:%M:%S',time.localtime(longtime))
    return s

# 3 读取文件信息
info = os.stat('test1.txt')
print(type(info),info)

print("最近一次访问时间",date_format(info.st_atime))
print("在Windows中显示文件的创建时间",date_format(info.st_ctime))
print("最后一次修改时间",date_format(info.st_mtime))
print("文件的大小（单位：字节）",info.st_size)


# 4 启动指定文件
os.startfile('test1.txt')
