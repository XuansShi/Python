# 示例10-25：jieba分词
import jieba
# 读取文件
with open('jieba.txt','r',encoding="utf-8") as file:
    s=file.read()

# 分词
lst=jieba.lcut(s)

# 利用集合去掉重复
set1=set(lst)

# 使用字典统计词频
d={}   # key:词   value:某个词出现的次数
for item in set1:
    if len(item)>=2:
        d[item]=0

    # 遍历，统计出现次数
for item in lst:
    if item in d:
        d[item]=d.get(item)+1
    # 转成列表
new_lst = []
for item in d:
    new_lst.append([item,d[item]])

