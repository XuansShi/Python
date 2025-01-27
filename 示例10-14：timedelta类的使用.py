# 示例10-14：timedelta类的使用
from datetime import datetime, timedelta
# 两个datetime类型的对象
    # 通过相减创建timedelta对象
delta1=datetime(2028,10,1)-datetime(2028,5,1)
print("delta1:",delta1,type(delta1))

    # 通过传参创建一个timedelta对象
td1=timedelta(10)
print("td1:",td1,type(td1))
td2=timedelta(10,1)
print("td2:",td2,type(td2))















