# 第11章-实战题四：模块淘宝自动回复
def find_answer(question):
    with open("replay.txt", "r",encoding="utf-8") as file:
        while True:
            line = file.readline()
            if line=="":
                break # 退出while循环
            # 字符串的劈分操作
            keyword = line.split("|")[0]
            reply=line.split("|")[1]
            if keyword in question:
                return reply
    return  False


if __name__=="__main__":
    question=input("请输入您的问题")
    while True:
        if question=='bye':
            break
        else:
            reply=find_answer(question)
            if reply == False:
                question=input("不知道您在是什么，您可以询问一些关于订单、物流、账户方面的问题，退出请输入bye：")
            else:
                print(reply)
                question=input("您可以询问一些关于订单、物流、账户方面的问题，退出请输入bye：")
    print("再见")





