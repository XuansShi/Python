#示例4-21： continue在for循环中的使用
print("敲桌子小游戏：")
for i in range(100):
    if i%7 ==0 or i//7 == 0 or (i%10) == 7:
        continue
    else:
        print(i)








