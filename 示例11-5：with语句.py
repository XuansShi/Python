# 示例11-5：with语句
# 写
def write_fun():
    with open('test5.txt','w',encoding="utf-8") as file:
        file.write("得得得得得得得得得得得得得得得得得得得得得得得得")
    # 使用with语句打开文件后就不需要手动关闭文件了

# 读
def read_fun():
    with open('test5.txt','r',encoding="utf-8") as file:
        print(file.read())

# 复制
def copy(src_file,target_file):
    with open(src_file,'r',encoding="utf-8") as file:# 先读再写
        with open(target_file,'w',encoding="utf-8") as file2:# 先读再写
            file2.write(file.read()) # 将读取的文件直接写入


if __name__ == '__main__':
    write_fun()
    read_fun()

    # 文件复制
    copy('./test5.txt','./test6.txt')


