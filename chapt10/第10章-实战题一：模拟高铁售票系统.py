# 第10章-实战题一：模拟高铁售票系统
import  prettytable as pt

# 创建座位函数
def show_ticket(row_num):
    # 创建一张表格
    tb = pt.PrettyTable()
    # 设置表头
    tb.field_names=["行号","座位1","座位2","座位3","座位4","座位5"]
    # 遍历有票
    for i in range(1,row_num+1):
        lst=[f"第{i}行","有票","有票","有票","有票","有票"]
        tb.add_row(lst)
    # 打印
    print(tb)



# 订票函数
    # 重新绘制
def order_ticket(row_num,row,column):
    tb = pt.PrettyTable()# 创建一张表格
    tb.field_names=["行号","座位1","座位2","座位3","座位4","座位5"]# 设置表头
    for i in range(1,row_num+1):
        if int(row)==i:  # 遍历到与传入的行号相等时，将对应的 column列 的元素改为 售罄
            lst=[f"第{i}行","有票","有票","有票","有票","有票"]
            lst[int(column)]="售罄"
            tb.add_row(lst)
        else: # 不相等就正常显示
            lst = [f"第{i}行", "有票", "有票", "有票", "有票", "有票"]
            tb.add_row(lst)
    print(tb)


if __name__ == '__main__':
    row_num = 6
    show_ticket(row_num) # 6行

    # 售票
    choose_num=input("请输入您选择的座位。示例 4,3  :")
    row,column = choose_num.split(',') # 由于输入的中间有个逗号，可以用split进行劈分，实现系列解包赋值
    order_ticket(row_num,row,column)











