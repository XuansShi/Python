#示例5-10：列表生成式的使用
import random#包含随机数

#列表生成式-语法：
  # 1 ist = [expression for item in range] #从某列表中选择元素来组成新的列表
  # 2 ist = [expression for item in range if condition] #从某列表中选择符合条件的元素来组成新的列表


# 1 ist = [expression for item in range] #从某列表中选择元素来组成新的列表
lst=[item for item in range(1,11)]
print(lst)

lst=[item*item for item in range(1,11)]
print(lst)

lst=[random.randint(1,100) for _ in range(10)]#选取10个从 1 到 100 间的随机数来组成新的列表
print(lst)



# 2 ist = [expression for item in range if condition] #从某列表中选择符合条件的元素来组成新的列表
lst=[i for i in range(10) if i%2==0]
print(lst)