#第5章-实战题二
lst=[]
for i in range(5):
    goods=input("请输入需要加入购物车中的商品编号和名称，一次输入一件商品")
    lst.append(goods)

#输出所有商品信息
for item in lst:
    print(item)

#创建一个空列表，用来存储购物车中的商品
cart=[]
while True:
    flag  = False#代表没有商品的情况
    num=input("请输入要购买的商品编号，正确格式如：1001猫粮，1002狗粮")
    #遍历商品列表，查询要购买的商品品是否存在
    for item in lst:
        if num == item[0:4]:#切片操作 ，把每一个item字符串的前4位切出来
            flag = True#代表商品已经找到
            cart.append[item]
            print("商品已成功添加")
            break#退出for循环

    if not flag and num != 'q':  # not flag 等价于 flag==False
            print('商品不存在')

    if num == 'q':
            break  # 退出的才是while循环

print('-' * 50)
print('您购物车里已选择的商品为:')
cart.reverse()
for item in cart:
    print(item)











