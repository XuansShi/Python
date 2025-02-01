# 第10章-实战题二： 推算几天后的日期
import  datetime

# 输入日期并且转换格式的函数
def input_date():
    inputdate=input("请输入开始日期 示例 (20281001) :")
    datestr=inputdate[0:4]+'-'+inputdate[4:6]+'-'+inputdate[6:8]  # 字符串切片拼接
    # 类型转换  年-月-日
    dt=datetime.datetime.strptime(datestr,'%Y-%m-%d')
    return dt

# 主程序运行
if __name__=='__main__':
    date = input_date()

    # 输入间隔天数
    in_num = eval(input("请输入间隔天数"))

    # 计算
    date = date + datetime.timedelta(days=in_num)

    # 打印
    print(date)













