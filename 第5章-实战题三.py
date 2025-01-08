#第5章-实战题三
#创建一个字典来存放列车的相关信息，使用列车编号作为键key，其他的信息作为value
dict_ticket={
    'G1569':['北京南-天津南','18:06','18:39','00:33'],
    'G1567':['北京南-天津南','18:15','18:49','00:34'],
    'G8917':['北京南-天津西','18:20','18:19',"00:59"],
    'G203':['北京南-天津南','18:35','19:09','00:34']
}



#遍历所以车次以及相关信息
print('车次     出发站-到达站    出发时间    到达时间    历时时长')

for key in dict_ticket.keys():
    print(key,end="  ")#不换行
    for value in dict_ticket[key]:# 根据key获取值
        print(value,end="\t\t")#这里的\t用于分隔每个value的四个元素
    print()


#买票：
train_no=input('请输入要购买的车次：')# 输入用户的购票车次


info=dict_ticket.get(train_no,'车次不存在')# 根据key获取value值，这里的train_no作为key；info来自value，所以是列表类型
                    #如果train_no不存在，赋予默认的value值 "车次不存在"

# 判断车次是否存在
if info!='车次不存在':
    person=input('请输入乘车人，如果是多位乘车人使用逗号分隔:')

    # 获取车次的出发站-到达站，还有出发时间
    s=info[0]+' '+info[1] +'开'#拼接列表类型info的各个元素

    print('您已购买了'+train_no+' '+s+',请'+person+'尽快换取纸制车示。【铁路客服】')

else:
    print('对不起，选择的车次可能不存在')
