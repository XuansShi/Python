# 示例10-11：random模块的使用
import  random

# seed(x) 设置随机数的种子
random.seed(10)

# 一、random
print(random.random())  # 产生0.0到1.0间的数，左闭右开
print(random.random())


# 二、randint(a,b)  产生a到b间的整数
print(random.randint(1,100)) # 1到100间的整数，左闭右开


# 三、randrange(m,n,k)  生成一个[m,n)范围间，步长为k的随机整数
for i in range(10):
    print(random.randrange(1,10,3))

# 四、 uniform(a,b)  生成[a,b]之间的随机小数
print(random.uniform(1,10))


# 五、choice(seq)
lst = [i for i in range(1,11)]
print(random.choice(lst))      #从列表中随机取出一个元素


# 六、shuffle(seq)  洗牌算法
print(random.shuffle(lst))













