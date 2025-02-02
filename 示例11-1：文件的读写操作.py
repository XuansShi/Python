# 示例11-1：文件的读写操作
# 创建并写入 函数
def my_write():
    # 1 创建/打开文件
    file = open('test.txt', 'w',encoding='utf-8') # 打开模式为"w" write
    # 2 操作文件
    file.write("啦啦啦啦啦")
    # 3 关闭文件
    file.close()

# 读取文件 函数
def my_read():
    file = open('test.txt', 'r',encoding='utf-8') # 打开模式为“r”  read
    s=file.read()
    print(type(s),s)
    file.close()

# 主程序运行
if __name__ == '__main__':
    my_write()

    my_read()





