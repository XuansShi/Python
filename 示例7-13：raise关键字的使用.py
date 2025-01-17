# 示例7-13：raise关键字的使用
try:
    gender=input('请输入您的性别:')
    if gender!='男'and gender!='女':
        raise Exception('性别只能是男或女') #raise抛出异常对象，用Exception接收
    else:
        print('您的性别是:',gender)

except Exception as e: # 此处的Exception接收异常对象；给Exception起个别名叫e
    print(e) # 打印异常的描述信息