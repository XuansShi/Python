#示例5-24：同步迭代
fruits=['apple','orange','pear','grape']#补充：如果你把这两个列表改成集合，由于集合是无序的，不一定能对上
counts=[10,3,4,5]

for f,c in zip(fruits,counts):#同时从列表fruits和列表counts中获取元素
    match f,c:
        case 'apple',10:
            print('10个苹果')
        case 'orange',3:
            print('3个桔子')
        case 'pear',4:
            print('4个梨')
        case 'grape',5:
            print('5串葡萄')
