#第5章-实战题一

#方法一、for遍历列表
lst=[98,95,93,99,91,00]#00本质是0
print(lst)

for index in range(len(lst)):
    if str(lst[index])!="0":#这里只能写"0"，不能写"00"
        lst[index]="19"+str(lst[index])
    else :
        lst[index]="200"+str(lst[index])

print(lst)

#方法二、enumerate + for
lst2=[98,95,93,99,91,96,00]
print(lst2)
for index,value in enumerate(lst2):
    if str(value)!="0":
        lst2[index]="19"+str(lst2[index])
    else:
        lst2[index]="200"+str(lst2[index])
print(lst2)