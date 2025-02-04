# 示例11-6：一维数据和二维数据的存储

# 一维数据，写入时要把列表转换为字符串；读取时要把字符串转为列表
def my_write():
    # 一维数据可以是列表 元组 集合
    lst=["张三","李四",'王五']
    with open ("student.txt","w") as file:# 默认的编码格式是GBK
        file.write(','.join(lst))

def my_read():
    with open('student.csv','r') as file:
        s=file.read()
        lst=s.split(',')
        print(lst)

# 二维数据 使用二维列表
def my_write_table():
    lst=[
        ['商品名称','单价','采购数量']
        ['a','10','20']


    ]
    with open('table.csv','w',encoding='utf-8') as file:
        for i in lst:
            line=','.join(i)
            file.write(line)
            file.write('\n')

def my_read_table():
    data=[]
    with open('table.csv','r',encoding='utf-8') as file:
        lst=file.readlines()
        #print(type(lst),lst)
        for i in lst:
            new_lst=i[:len(i)-1].split(',')
            data.append(new_lst)
    print(data)


if __name__ == '__main__':
    #my_write()
    #my_read()
    my_write_table()






