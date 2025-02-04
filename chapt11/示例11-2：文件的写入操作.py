# 示例11-2：文件的写入操作

# 将字符串写入文件
def my_write(s):
    # 1 打开或创建文件
    file = open('test2.txt', 'a',encoding='utf-8') # a追加写入模式;utf-8代表中文是三个字节

    # 2 写入内容
    file.write(s)
    file.write("\n")# 写入一行后换行

    # 3 关闭文件
    file.close()


# 将内容必须全部为字符串的列表写入文件
def my_write_list(file,lst):
    f = open(file,'a',encoding='utf-8')
    f.writelines(lst)
    f.close()


if __name__ == '__main__':
    my_write("来来来")
    my_write("啦啦啦啦啦啦啦")

    lst=['姓名\t','年龄\t','成绩\n','张三\t','12\t','90']
    my_write_list("file3.txt",lst)


