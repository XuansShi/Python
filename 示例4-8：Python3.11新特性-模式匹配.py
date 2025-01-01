#示例4-8：Python3.11新特性-模式匹配
score = input("请输入成绩等级：")
match score:
    case 'a':
        print("优秀")
    case 'b':
        print("良好")
    case 'c':
        print("中等")
#在c/c++中case后的条件只能是数字，Python里可以是其他的东西