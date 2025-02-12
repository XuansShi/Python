#示例6-12：sub函数与split函数的使用
import re
pattern='黑客|破解|反爬'

# (一)sub函数 实例-实现屏蔽词
s='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s) #参数： 第一个：模式字符串,第二个：替换字符,第三个：待sub字符串
print(new_s)

# (二)split函数
s2='https://www.baidu.com/s?wd=ysj&rsv_spt=1'
pattern2='[?|&]'  # 模式字符串：[] 代表在区间内；?和& 代表使用?和&进行分割; | 代表区间内的任何符号都可写
lst=re.split(pattern2,s2)
print(lst)








