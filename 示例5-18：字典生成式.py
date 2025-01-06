#示例5-18：字典生成式
# （1）使用for+random
import random
d={item :random.randint(1,100) for item in range(4)}# key键的取值 0 1 2 3 ； 元素取值是1~100的随机数
print(d)

# （2）使用映射的方式
lst=[1001,1002,1003]
lst2=['陈梅梅','王一一','李丽丽']
d={key:value for key,value in zip(lst,lst2)}
print(d)

