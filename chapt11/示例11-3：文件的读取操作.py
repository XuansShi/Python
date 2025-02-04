# 示例11-3：文件的读取操作
def my_read(filename):
    file =  open(filename,'w+',encoding='utf-8')# w+代表同时具有读取和写入功能
    file.write("nihao")

    #seek 修改文件指针的位置
    file.seek(0)

    # 读取
    # s=file.read()# 读取全部
    # s=file.read(2)# 读取2个字符
    # s=file.readline()# 读取一行
    # s=file.readline(2)# 读取一行中的两个字符
    # s=file.readlines()# 读取所有，一行为列表中的一个元素，此时s为list类型

    # 读取"hao"
    file.seek(2)
    s=file.read()

    print(type(s),s)

    # 关闭
    file.close()

if __name__ == '__main__':
    my_read('test4.txt')




