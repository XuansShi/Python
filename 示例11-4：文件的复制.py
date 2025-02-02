# 示例11-4：文件的复制
def copy(src,new_path):
    # 文件的复制是边读边写操作
    # 1 打开源文件
    file1=open(src,'rb')# 打开二进制文件

    # 2 打开目标文件
    file2 = open(new_path,'wb')

    # 3 开始复制，边读边写
    s = file1.read()
    file2.write(s)

    # 4 关闭
    file2.close()
    file1.close()# 类似栈的“先进后出”，先打开的文件后关,后打开的先关

if __name__ == '__main__':
    src="../chapt10/x1s0.jpg"   # ../代表 相对于本文件的 上级目录
    new_path="./x1s0cp.jpg" # ./代表 相对于本文件的 当前目录（相对路径）
    copy(src,new_path)
    print("文件复制完毕")






